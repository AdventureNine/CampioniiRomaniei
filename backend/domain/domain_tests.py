from backend.domain.entities.FillInStatement import FillInStatement
from backend.domain.entities.Minigame import Puzzle, Rebus, Bingo, Pairs, MapGuesser
from backend.domain.entities.Player import Player
from backend.domain.entities.Question import Question
from backend.domain.entities.Quizz import Quizz
from backend.domain.utils.Difficulty import Difficulty

def test_player(player: Player):
    assert (player.get_name() == "nume")
    assert (player.get_credits() == 0)
    assert (player.get_cosmetic() == "/backend/domain/cosmetics/default.png")
    assert (player.get_statistics()["quizzes_solved"] == 0)
    assert (player.get_statistics()["quizzes_played"] == 0)
    assert (player.get_statistics()["regions_unlocked"] == ["Transilvania"])
    assert (player.get_statistics()["cosmetics_unlocked"] == ["/backend/domain/cosmetics/default.png"])
    assert (player.get_statistics()["cosmetics_purchased"] == ["/backend/domain/cosmetics/default.png"])
    assert (player.get_statistics()["completion_percentage"] == 0.0)
    assert (player.get_id() == 1)

def test_quizz(quizz: Quizz, singleResponseQuestion: Question, multipleResponseQuestion: Question, fill_in_statement: FillInStatement, answers: list[str]):
    assert (multipleResponseQuestion.check_answers(answers))
    assert (multipleResponseQuestion.check_answers(["a"]))
    assert (not multipleResponseQuestion.check_answers(["z"]))
    assert (singleResponseQuestion.check_answers([answers[2]]))
    assert (not singleResponseQuestion.check_answers(["a"]))
    assert (singleResponseQuestion.get_text() == "Lorem ipsum dolor sit amet, consectetur adipiscing elit?")
    assert (multipleResponseQuestion.get_text() == "Lorem ipsum dolor sit amet, consectetur adipiscing elit?")
    assert (fill_in_statement.get_text_segments() == ["lorem ipsum", "dolor sit amet", ", consectetur adipiscing elit"])
    assert (fill_in_statement.check_answers(["a", "b", "c", "d"]))
    assert (not fill_in_statement.check_answers(["a", "b", "c", "serdghrtj"]))

    assert (quizz.get_completion_percentage() == 15.3)
    assert (quizz.get_difficulty() == Difficulty[1])
    assert (len(quizz.get_minigames()) == 5)
    assert (quizz.get_questions()[0] == singleResponseQuestion)
    assert (quizz.get_questions()[1] == multipleResponseQuestion)
    assert (quizz.get_fill_in_statements()[0] == fill_in_statement)

    assert (quizz.get_minigames()[0].get_image_path() == "dummy")
    assert (quizz.get_minigames()[1].get_win_configuration() == {"intrebare1": "raspuns1", "intrebare2": "raspuns2", "intrebare3": "raspuns3"})
    assert (quizz.get_minigames()[2].get_win_configuration() == {"bingo_cell1_text": True, "bingo_cell2_text": False, "bingo_cell3_text": True, "bingo_cell4_text": False})
    assert (quizz.get_minigames()[3].get_win_configuration() == {"question1": "answer1", "question2": "answer2", "question3": "answer3"})
    assert (quizz.get_minigames()[4].get_win_configuration() == [(1,2), (2,1), (3,4), (4,3)])


def test_domain():
    answers = ["a", "b", "c", "d"]
    fill_in_statement = FillInStatement(1, ["lorem ipsum", "dolor sit amet", ", consectetur adipiscing elit"], answers)
    singleResponseQuestion = Question(1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit?", [answers[2]])
    multipleResponseQuestion = Question(2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit?", answers)
    puzzle = Puzzle(1, "dummy")
    rebus = Rebus(1, {"intrebare1": "raspuns1", "intrebare2": "raspuns2", "intrebare3": "raspuns3"})
    bingo = Bingo(1, {"bingo_cell1_text": True, "bingo_cell2_text": False, "bingo_cell3_text": True, "bingo_cell4_text": False})
    pairs = Pairs(1, {"question1": "answer1", "question2": "answer2", "question3": "answer3"})
    mapGuesser = MapGuesser(1, [(1,2), (2,1), (3,4), (4,3)])
    quizz = Quizz(1, [singleResponseQuestion, multipleResponseQuestion], [fill_in_statement], [puzzle, rebus, bingo, pairs, mapGuesser], Difficulty[1],15.3)
    player = Player(1, "nume")

    test_quizz(quizz, singleResponseQuestion, multipleResponseQuestion, fill_in_statement, answers)
    test_player(player)

    print(puzzle)
    print(rebus)
    print(bingo)
    print(pairs)
    print(mapGuesser)
    print(fill_in_statement)
    print(singleResponseQuestion)
    print(multipleResponseQuestion)
    print(quizz)
    print(player)

test_domain()