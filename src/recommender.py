def get_recommendations(intrinsic, extraneous, germane):
    rec = []
    precautions = []

    if extraneous == "High":
        rec += [
            "Reduce distractions",
            "Use Pomodoro technique",
            "Find quieter place"
        ]
        precautions.append("Avoid multitasking")

    if intrinsic == "High":
        rec += [
            "Break topic into smaller parts",
            "Switch to easier topics"
        ]

    if germane == "Low":
        rec += [
            "Use active recall",
            "Practice questions"
        ]

    if intrinsic == "Low" and extraneous == "Low" and germane == "High":
        rec.append("Optimal learning state. Keep going!")

    return rec, precautions