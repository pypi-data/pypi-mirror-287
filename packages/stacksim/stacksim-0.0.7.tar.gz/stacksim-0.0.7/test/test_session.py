import sys
import os

from stacksim.stackSession import StackSession

def test_session():

    session = StackSession()

    session.parseCommand("int i =42")

    wordCount = len(session.stack.currentFrame.cells[0].words)
    wordValue = session.stack.currentFrame.cells[0].words[0].value

    assert wordCount == 1
    assert wordValue == 42


if __name__ == "__main__":
    test_session()