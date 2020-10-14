import numpy as np


def c(*args):
    """ R에서 벡터를 만드는데 사용되는 명령어.
    numpy.array()와 똑같이 작용

    :param args: 배열 안에 넣을 원소들
    :return: numpy 배열
    """
    return np.array(args)


def seq(from_, to_, **kwargs):
    """ R에서 sequence(순차적인 값들의 벡터)를 만들 때 사용하는 함수

    :param from_: sequence의 처음 값
    :param to_: sequence의 마지막 값
    :param kwargs: by: 원소들 간 간격 / length_out: 원소의 개수
    :return:
    """
    if not isinstance(from_, int) and not isinstance(from_, float):
        raise TypeError("첫번째 인자의 타입이 숫자가 아닙니다.")
    elif not isinstance(to_, int) and not isinstance(to_, float):
        raise TypeError("두번째 인자가 타입이 숫자가 아닙니다.")
    pass


def seq_int():
    """ R의 seq.int()
    """
    pass


def seq_len():
    """ R의 seq_len()
    """
    pass


def rep(x, **kwargs):
    """ R에서 repeat 반복되는 값들의 벡터를 만들 때 사용하는 함수

    :param x:
    :param kwargs:
    :return:
    """
    if not isinstance(x, int) and not isinstance(x, float):
        raise TypeError("인자의 타입이 숫자가 아닙니다.")
    pass

def rep_int():
    """ R의 rep.int()
    """
    pass


def rep_len():
    """ R의 rep_len()
    """
    pass
