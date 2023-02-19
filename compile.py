import subprocess
import sys


def runPython(filePath):
    file = open(filePath, 'r')
    result = subprocess.run(
        [sys.executable, "-c", file.read()], capture_output=True, text=True, timeout=1
    )

    # Prints out successful shell output
    stdout = result.stdout

    # Prints out error messages
    stderr = result.stderr
    output = stdout + stderr

    file.close()
    return output


def runJavaScript(filePath):

    # follows same process as above
    result = subprocess.run(
        ['node', filePath], capture_output=True, text=True, timeout=1)

    stdout = result.stdout
    stderr = result.stderr
    output = stdout + stderr

    return output


def runCode(language, filePath):
    output = ''
    if language == 'python':
        output = runPython(filePath)
    elif language == 'javascript':
        output = runJavaScript(filePath)

    return output