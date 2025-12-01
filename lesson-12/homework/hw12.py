import threading

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end, result):
    """Find primes in a given range and append to shared result list."""
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)


def main():
    start_range = int(input("Enter start of range: "))
    end_range = int(input("Enter end of range: "))
    num_threads = int(input("Enter number of threads: "))

    threads = []
    primes = []
    step = (end_range - start_range + 1) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step - 1 if i < num_threads - 1 else end_range
        t = threading.Thread(target=find_primes_in_range, args=(start, end, primes))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    primes.sort()
    print("\nPrime numbers found:", primes)


if __name__ == "__main__":
    main()

import threading
from collections import Counter

def process_lines(lines, counter):
    """Count words in a subset of lines."""
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)


def threaded_word_count(file_path, num_threads=4):
    """Split file among threads and count word occurrences."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    counters = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else total_lines
        t = threading.Thread(target=process_lines, args=(lines[start:end], counters))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    print("\n📊 Word Frequency Summary:")
    for word, count in total_counter.most_common(10):
        print(f"{word}: {count}")


if __name__ == "__main__":
    file_path = input("Enter file path: ")
    threaded_word_count(file_path, num_threads=4)
