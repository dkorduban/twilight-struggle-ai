#pragma once

#include <chrono>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <optional>
#include <sstream>
#include <string>
#include <string_view>
#include <utility>

namespace ts::experimental::logging {

inline std::string prefix(const char* file, int line) {
    const auto now = std::chrono::system_clock::now();
    const auto tt = std::chrono::system_clock::to_time_t(now);
    const auto micros = std::chrono::duration_cast<std::chrono::microseconds>(now.time_since_epoch()).count() % 1000000;
    std::tm tm{};
#if defined(_WIN32)
    localtime_s(&tm, &tt);
#else
    localtime_r(&tt, &tm);
#endif
    std::ostringstream out;
    out << std::put_time(&tm, "%Y-%m-%d %H:%M:%S")
        << "." << std::setw(6) << std::setfill('0') << micros
        << " " << file << ":" << line << " ";
    return out.str();
}

class TeeLogger {
public:
    explicit TeeLogger(std::optional<std::string> file_path = std::nullopt)
        : file_path_(std::move(file_path)) {
        std::cout.setf(std::ios::unitbuf);
        if (file_path_ && !file_path_->empty()) {
            file_.emplace(*file_path_, std::ios::out | std::ios::trunc);
            file_->setf(std::ios::unitbuf);
        }
    }

    template <typename... Args>
    void log(const char* file, int line, Args&&... args) {
        write_line(std::cout, file, line, std::forward<Args>(args)...);
        if (file_) {
            write_line(*file_, file, line, std::forward<Args>(args)...);
        }
    }

    template <typename... Args>
    void raw(Args&&... args) {
        write_raw(std::cout, std::forward<Args>(args)...);
        if (file_) {
            write_raw(*file_, std::forward<Args>(args)...);
        }
    }

private:
    template <typename... Args>
    static void write_line(std::ostream& out, const char* file, int line, Args&&... args) {
        out << prefix(file, line);
        (out << ... << std::forward<Args>(args));
        out << '\n';
    }

    template <typename... Args>
    static void write_raw(std::ostream& out, Args&&... args) {
        (out << ... << std::forward<Args>(args));
    }

    std::optional<std::string> file_path_;
    std::optional<std::ofstream> file_;
};

}  // namespace ts::experimental::logging

#define TS_EXP_LOG(logger, ...) (logger).log(__FILE__, __LINE__, __VA_ARGS__)
