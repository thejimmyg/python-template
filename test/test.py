import myproject.__main__ as main
from io import StringIO
from myproject import inc


def test_answer():
    assert inc(3) == 4


def test_main(mocker):
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    main.main()
    assert mock_stdout.getvalue() == '''Running ...
inc(3)=4
done.
'''

