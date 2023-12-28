def abba(newScore: int) -> Exception:
    me = 'The new score is: '
    try:
        m = open('score.dat', 'a')
        m.write(f'{me}{newScore}\n')
    except Exception as e:
        return e



