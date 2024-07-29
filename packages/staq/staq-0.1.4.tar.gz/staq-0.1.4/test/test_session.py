import sys
import os

from staq.stackSession import StackSession

def test_session():

    session = StackSession()

    session.parseCommand("int i =42")

    wordCount = len(session.stack.currentFrame.cells[0].words)
    wordValue = session.stack.currentFrame.cells[0].words[0].value

    assert wordCount == 1
    assert wordValue == 42

def test_html():
    session = StackSession()

    session.parseCommand("int etc[64]")
    session.parseCommand("call main()")
    session.parseCommand("int buf[16]")
    session.parseCommand('run printf("Hello %d %d", 1, 2)')

    html = session.stack.toHtml()

    with open("test.html", "w") as fh:
        fh.write(html)


if __name__ == "__main__":
    test_session()