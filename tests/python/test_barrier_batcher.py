"""Unit tests for BarrierBatcher from scripts/collect_learned_vs_heuristic.py"""

import sys
import os
import threading
import time
import pytest
import torch

# Import BarrierBatcher from the scripts directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../scripts'))
from collect_learned_vs_heuristic import BarrierBatcher


class MockModel:
    """Simple mock model that records calls and returns fixed-size tensors."""

    def __init__(self, influence_dim=128, cards_dim=111, scalars_dim=32):
        self.call_count = 0
        self.last_batch_size = 0
        self.call_log = []  # List of (batch_size, shapes) tuples
        self.influence_dim = influence_dim
        self.cards_dim = cards_dim
        self.scalars_dim = scalars_dim

    def __call__(self, influence, cards, scalars):
        self.call_count += 1
        batch_size = influence.shape[0]
        self.last_batch_size = batch_size
        self.call_log.append({
            'batch_size': batch_size,
            'influence_shape': tuple(influence.shape),
            'cards_shape': tuple(cards.shape),
            'scalars_shape': tuple(scalars.shape),
        })
        return {
            "card_logits": torch.zeros(batch_size, 111),
            "value": torch.zeros(batch_size, 1),
        }

    def eval(self):
        return self


def make_dummy_features(batch_size=1, influence_dim=128, cards_dim=111, scalars_dim=32, device='cpu'):
    """Create dummy feature tensors for testing."""
    return (
        torch.randn(batch_size, influence_dim, device=device),
        torch.randn(batch_size, cards_dim, device=device),
        torch.randn(batch_size, scalars_dim, device=device),
    )


@pytest.mark.timeout(10)
def test_basic_full_batch_inference():
    """Test that a full batch of requests triggers inference exactly once."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=4, device=device)
    batcher.set_active_slots(4)

    results = {}
    results_lock = threading.Lock()

    def worker(slot_id):
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results[slot_id] = result

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert model.call_count == 1, f"Expected 1 model call, got {model.call_count}"
    assert model.last_batch_size == 4, f"Expected batch size 4, got {model.last_batch_size}"
    assert len(results) == 4, f"Expected 4 results, got {len(results)}"
    for slot_id in range(4):
        assert slot_id in results
        assert "card_logits" in results[slot_id]
        assert results[slot_id]["card_logits"].shape[0] == 1


@pytest.mark.timeout(10)
def test_partial_batch_via_deactivate():
    """Test that deactivating a slot before requests triggers batch with fewer slots."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=4, device=device)
    batcher.set_active_slots(4)

    # Deactivate slot 3 before any requests
    batcher.deactivate_slot(3)

    results = {}
    results_lock = threading.Lock()

    def worker(slot_id):
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results[slot_id] = result

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert model.call_count == 1, f"Expected 1 model call, got {model.call_count}"
    assert model.last_batch_size == 3, f"Expected batch size 3, got {model.last_batch_size}"
    assert len(results) == 3, f"Expected 3 results, got {len(results)}"


@pytest.mark.timeout(10)
def test_deactivate_while_inflight():
    """Test that deactivating a slot while requests are in-flight triggers batch."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=3, device=device)
    batcher.set_active_slots(3)

    results = {}
    results_lock = threading.Lock()
    event_slot0_started = threading.Event()
    event_slot1_started = threading.Event()

    def worker(slot_id):
        if slot_id == 0:
            event_slot0_started.set()
            time.sleep(0.1)  # Delay so slot 1 also starts
        elif slot_id == 1:
            event_slot1_started.set()
            time.sleep(0.1)  # Delay so deactivate happens before request

        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results[slot_id] = result

    # Start threads 0 and 1
    thread0 = threading.Thread(target=worker, args=(0,))
    thread1 = threading.Thread(target=worker, args=(1,))
    thread0.start()
    thread1.start()

    # Wait for both to signal they've started, then deactivate slot 2
    event_slot0_started.wait()
    event_slot1_started.wait()
    time.sleep(0.05)  # Small delay to ensure requests are buffered
    batcher.deactivate_slot(2)

    thread0.join()
    thread1.join()

    # Model should have been called once with batch size 2 (slots 0,1)
    assert model.call_count == 1, f"Expected 1 model call, got {model.call_count}"
    assert model.last_batch_size == 2, f"Expected batch size 2, got {model.last_batch_size}"
    assert 0 in results and 1 in results


@pytest.mark.timeout(10)
def test_sequential_batches():
    """Test multiple sequential batches (3 rounds with 2 slots each)."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=2, device=device)

    for round_num in range(3):
        batcher.set_active_slots(2)
        results = {}
        results_lock = threading.Lock()

        def worker(slot_id):
            influence, cards, scalars = make_dummy_features(device=device)
            result = batcher.request(slot_id, influence, cards, scalars)
            with results_lock:
                results[slot_id] = result

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert len(results) == 2, f"Round {round_num}: expected 2 results, got {len(results)}"

    assert model.call_count == 3, f"Expected 3 model calls total, got {model.call_count}"
    for i, log_entry in enumerate(model.call_log):
        assert log_entry['batch_size'] == 2, f"Call {i}: expected batch size 2, got {log_entry['batch_size']}"


@pytest.mark.timeout(10)
def test_set_active_slots_resets_state():
    """Test that set_active_slots resets state between rounds."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=2, device=device)

    # First round
    batcher.set_active_slots(2)
    results1 = {}
    results_lock = threading.Lock()

    def worker(slot_id, results_dict):
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results_dict[slot_id] = result

    threads = [threading.Thread(target=worker, args=(i, results1)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert model.call_count == 1

    # Second round with fresh set_active_slots
    batcher.set_active_slots(2)
    results2 = {}
    threads = [threading.Thread(target=worker, args=(i, results2)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert model.call_count == 2, f"Expected 2 total model calls, got {model.call_count}"
    assert len(results2) == 2, "Second round should have 2 results"


@pytest.mark.timeout(10)
def test_deactivate_all_slots_no_deadlock():
    """Test that deactivating all slots doesn't cause deadlock."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=3, device=device)
    batcher.set_active_slots(3)

    # Deactivate all slots without any requests
    batcher.deactivate_slot(0)
    batcher.deactivate_slot(1)
    batcher.deactivate_slot(2)

    # Should complete without deadlock; no model calls since no requests
    assert model.call_count == 0, f"Expected 0 model calls, got {model.call_count}"


@pytest.mark.timeout(10)
def test_result_isolation():
    """Test that each slot gets its own result (not shared buffers)."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=2, device=device)
    batcher.set_active_slots(2)

    results = {}
    results_lock = threading.Lock()

    def worker(slot_id):
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results[slot_id] = result

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Each result should have batch size 1 (single-slot slice)
    assert results[0]["card_logits"].shape == (1, 111)
    assert results[1]["card_logits"].shape == (1, 111)

    # Results should be independent (cloned, not views)
    # Verify by checking they're different tensor objects
    assert results[0]["card_logits"] is not results[1]["card_logits"]


@pytest.mark.timeout(10)
def test_invalid_slot_id_raises():
    """Test that requesting on an inactive slot raises RuntimeError."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=2, device=device)
    batcher.set_active_slots(1)  # Only slot 0 is active

    influence, cards, scalars = make_dummy_features(device=device)

    with pytest.raises(RuntimeError, match="slot 1 is not active"):
        batcher.request(1, influence, cards, scalars)


@pytest.mark.timeout(10)
def test_set_active_slots_validation():
    """Test that set_active_slots validates input."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=4, device=device)

    # Valid calls
    batcher.set_active_slots(0)
    batcher.set_active_slots(4)

    # Invalid calls
    with pytest.raises(ValueError, match="active slot count must be in"):
        batcher.set_active_slots(-1)

    with pytest.raises(ValueError, match="active slot count must be in"):
        batcher.set_active_slots(5)


@pytest.mark.timeout(10)
def test_mixed_deactivations_and_requests():
    """Test a complex scenario: deactivate some slots, make requests, deactivate more."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=4, device=device)
    batcher.set_active_slots(4)

    # Deactivate slots 2 and 3
    batcher.deactivate_slot(2)
    batcher.deactivate_slot(3)

    results = {}
    results_lock = threading.Lock()

    def worker(slot_id):
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results[slot_id] = result

    # Request from slots 0 and 1 (the only active ones)
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert model.call_count == 1
    assert model.last_batch_size == 2
    assert len(results) == 2


@pytest.mark.timeout(10)
def test_feature_buffer_initialization():
    """Test that feature buffers are lazily initialized and reused."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=2, device=device)
    batcher.set_active_slots(2)

    # Buffers should be None initially
    assert batcher._influence_buf is None
    assert batcher._cards_buf is None
    assert batcher._scalars_buf is None

    results = {}
    results_lock = threading.Lock()

    def worker(slot_id):
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(slot_id, influence, cards, scalars)
        with results_lock:
            results[slot_id] = result

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Buffers should now be initialized
    assert batcher._influence_buf is not None
    assert batcher._cards_buf is not None
    assert batcher._scalars_buf is not None
    assert batcher._influence_buf.shape[0] == 2  # n_slots dimension


@pytest.mark.timeout(10)
def test_concurrent_requests_single_slot():
    """Test that multiple sequential requests from the same slot work correctly."""
    model = MockModel()
    device = torch.device('cpu')
    batcher = BarrierBatcher(model, n_slots=1, device=device)

    # Run 3 sequential rounds with the same slot
    for round_num in range(3):
        batcher.set_active_slots(1)
        influence, cards, scalars = make_dummy_features(device=device)
        result = batcher.request(0, influence, cards, scalars)
        assert "card_logits" in result
        assert result["card_logits"].shape == (1, 111)

    assert model.call_count == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
