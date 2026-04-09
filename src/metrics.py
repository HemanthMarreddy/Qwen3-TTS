def calculate_rtf(total_time, audio_duration):
    return total_time / audio_duration

def print_metrics(latency, audio_duration):
    rtf = calculate_rtf(latency, audio_duration)

    print("\n===== METRICS =====")
    print(f"Total Latency: {latency:.2f} sec")
    print(f"Audio Duration: {audio_duration:.2f} sec")
    print(f"RTF: {rtf:.2f}")