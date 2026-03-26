#include <pybind11/pybind11.h>

// ---------------------------------------------------------------------------
// Python bindings for the tscore C++ engine.
//
// This file is a stub.  Bindings for PublicState, HandKnowledge, and the
// reducer will be added as those interfaces stabilise.
// ---------------------------------------------------------------------------

namespace py = pybind11;

PYBIND11_MODULE(tscore, m) {
    m.doc() = "Twilight Struggle exact game engine (C++ core)";

    // Stub: no symbols exported yet.
    // Next bindings to add:
    //   - ts::PublicState (read-only view, hash accessor)
    //   - ts::HandKnowledge (read-only view, support mask accessor)
    //   - reduce(PublicState, ReplayEvent) -> PublicState
}
