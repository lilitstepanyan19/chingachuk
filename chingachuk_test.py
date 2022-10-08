import chingachuk as c
import pytest

game_piece = ['p', 's', 'r']


def test_game_res1():
    assert c.game_res('p', 'r', ['p', 's', 'r']) == 'comp - r, you - p, res - you won'

def test_game_res2():
    assert c.game_res('r', 'r', ['p', 's', 'r']) == 'comp - r, you - r, res - draw'    

def test_game_res3():
    assert c.game_res('s', 'r', ['p', 's', 'r']) == 'comp - r, you - s, res - you lost'

def test_game_res4():
    assert c.game_res('r', 's', ['p', 's', 'r']) == 'comp - s, you - r, res - you lost'

def test_game_res5():
    assert c.game_res('s', 's', ['p', 's', 'r']) == 'comp - s, you - s, res - draw'    

def test_game_res6():
    assert c.game_res('p', 's', ['p', 's', 'r']) == 'comp - s, you - p, res - you lost'

def test_game_res7():
    assert c.game_res('s', 'p', ['p', 's', 'r']) == 'comp - p, you - s, res - you won'

def test_game_res8():   
    assert c.game_res('p', 'p', ['p', 's', 'r']) == 'comp - p, you - p, res - draw'    

def test_game_res9():
    assert c.game_res('r', 'p', ['p', 's', 'r']) == 'comp - p, you - r, res - you won'
          
def test_get_game_with_comp1():
    assert c.get_game_with_comp(['p', 's', 'r']) == 'This piece not found' 

# def test_get_game_with_comp2(inp_piece, game_piece_k, game_piece):
#     assert c.get_game_with_comp(['p', 's', 'r']) == c.game_res(inp_piece, game_piece_k, game_piece)          
          
                
if __name__ == '__main__':
    pytest.main()