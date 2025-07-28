def classify(command):
    if 'wget' in command or 'curl' in command:
        return "Potential Malware Download"
    elif 'rm -rf' in command:
        return "Destructive Command"
    return "Unknown Behavior"