"""
Service Tests - Testing all services with existing database
Uses only extraction functions (no save/add operations)
Uses the database from backend/domain/data.db
"""

import sqlite3
import os
from backend.domain.entities.FillInStatement import FillInStatement
from backend.domain.entities.Player import Player
from backend.domain.entities.Question import Question
from backend.domain.entities.Quizz import Quizz
from backend.domain.entities.Minigame import Puzzle, Rebus, Bingo, MapGuesser
from backend.domain.utils.Difficulty import Difficulty

from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository
from backend.repository.RegionRepository import RegionRepository

from backend.service.PlayerService import PlayerService
from backend.service.QuestionService import QuestionService
from backend.service.FillInStatementService import FillInStatementService
from backend.service.MinigameService import MinigameService
from backend.service.QuizzService import QuizzService
from backend.service.QuizzTaskService import QuizzTaskService
from backend.service.RegionService import RegionService
from backend.service.GameService import GameService


# ==================== DATABASE SETUP ====================

# Path to the existing database in domain
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'domain', 'data.db'))


def get_database_connection() -> sqlite3.Connection:
    """
    Returns a connection to the existing database from domain.
    Only reads data, does not modify anything.
    """
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")
    
    con = sqlite3.connect(DB_PATH)
    return con


# ==================== SERVICE TESTS ====================

def test_player_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing PlayerService )---------------<")
    
    repo = PlayerRepository(con)
    service = PlayerService(repo)
    
    # Test get_player
    player = service.get_player()
    if player:
        print(f"get_player(): {player.get_name()} (ID: {player.get_id()})")
        assert player.get_id() is not None, "Player should have an ID!"
        assert player.get_name() is not None, "Player should have a name!"
        
        # Test get credits
        credits = player.get_credits()
        print(f"Player credits: {credits}")
        assert isinstance(credits, int), "Credits should be an integer!"
        
        # Test get statistics
        stats = player.get_statistics()
        print(f"Player statistics: {stats}")
        assert isinstance(stats, dict), "Statistics should be a dictionary!"
    else:
        print("get_player(): No player found in database")
    
    print(">--------------( PlayerService tests passed! )---------------<\n")
    return True


def test_question_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing QuestionService )---------------<")
    
    repo = QuestionRepository(con)
    service = QuestionService(repo)
    
    # Test get_questions_by_quizz - try different quizz IDs
    for quizz_id in [1, 2, 3]:
        questions = service.get_questions_by_quizz(quizz_id)
        print(f"get_questions_by_quizz({quizz_id}): {len(questions)} questions found")
        
        if questions:
            q = questions[0]
            print(f"  First question: {q.get_text()[:50]}..." if len(q.get_text()) > 50 else f"  First question: {q.get_text()}")
            
            # Test get_correct_answer
            correct = service.get_correct_answer(q.get_id())
            print(f"  get_correct_answer({q.get_id()}): {correct}")
            assert correct is not None, "Should have a correct answer!"
            
            # Test check_answer with correct answer
            is_correct = service.check_answer(q.get_id(), correct)
            print(f"  check_answer with correct: {is_correct}")
            assert is_correct, "Should be True for correct answer!"
            
            # Test check_answer with wrong answer
            is_wrong = service.check_answer(q.get_id(), "wrong_answer_xyz")
            print(f"  check_answer with wrong: {is_wrong}")
            assert not is_wrong, "Should be False for wrong answer!"
            
            # Test get_all_options
            options = service.get_all_options(q.get_id())
            print(f"  get_all_options({q.get_id()}): {len(options)} options")
            assert isinstance(options, list), "Options should be a list!"
            break  # Test one quizz only
    
    print(">--------------( QuestionService tests passed! )---------------<\n")
    return True


def test_fill_in_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing FillInStatementService )---------------<")
    
    repo = FillInStatementRepository(con)
    service = FillInStatementService(repo)
    
    # Test get_fill_ins_by_quizz - try different quizz IDs
    for quizz_id in [1, 2, 3, 4, 5]:
        fill_ins = service.get_fill_ins_by_quizz(quizz_id)
        print(f"get_fill_ins_by_quizz({quizz_id}): {len(fill_ins)} fill-ins found")
        
        if fill_ins:
            f = fill_ins[0]
            print(f"  First fill-in segments: {f.get_text_segments()[:3]}...")
            print(f"  First fill-in answers: {f.get_answer_list()}")
            
            # Test get_text_with_blanks
            text_blanks = service.get_text_with_blanks(f.get_id())
            print(f"  get_text_with_blanks({f.get_id()}): {text_blanks[:50]}..." if len(text_blanks) > 50 else f"  get_text_with_blanks: {text_blanks}")
            
            # Test get_answer_count
            count = service.get_answer_count(f.get_id())
            print(f"  get_answer_count({f.get_id()}): {count}")
            assert count >= 0, "Answer count should be non-negative!"
            
            # Test check_answers with correct answers
            correct_answers = f.get_answer_list()
            is_correct = service.check_answers(f.get_id(), correct_answers)
            print(f"  check_answers with correct: {is_correct}")
            break  # Test one quizz only
    
    print(">--------------( FillInStatementService tests passed! )---------------<\n")
    return True


def test_minigame_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing MinigameService )---------------<")
    
    repo = MinigameRepository(con)
    service = MinigameService(repo)
    
    # Test get_minigames_by_quizz - try different quizz IDs
    for quizz_id in [1, 2, 3, 4, 5]:
        minigames = service.get_minigames_by_quizz(quizz_id)
        print(f"get_minigames_by_quizz({quizz_id}): {len(minigames)} minigames found")
    
    # Try to find and test minigames by ID
    for mg_id in range(1, 20):
        minigame = service.get_minigame_by_id(mg_id)
        if minigame:
            mg_type = service.get_minigame_type(minigame)
            print(f"get_minigame_by_id({mg_id}): type={mg_type}")
            # Accept all known minigame types
            valid_types = ['puzzle', 'rebus', 'bingo', 'map_guesser', 'pairs']
            assert mg_type in valid_types, f"Unknown minigame type: {mg_type}"
    
    print(">--------------( MinigameService tests passed! )---------------<\n")
    return True


def test_quizz_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing QuizzService )---------------<")
    
    quizz_repo = QuizzRepository(con)
    question_repo = QuestionRepository(con)
    fill_in_repo = FillInStatementRepository(con)
    minigame_repo = MinigameRepository(con)
    
    service = QuizzService(quizz_repo, question_repo, fill_in_repo, minigame_repo)
    
    # Test get_all_quizzes
    all_quizzes = service.get_all_quizzes()
    print(f"get_all_quizzes(): {len(all_quizzes)} quizzes found")
    
    # Test get_quizz_by_id for first available quizz
    if all_quizzes:
        quizz_id = all_quizzes[0].get_id()
        quizz = service.get_quizz_by_id(quizz_id)
        if quizz:
            print(f"\nget_quizz_by_id({quizz_id}):")
            print(f"  Difficulty: {quizz.get_difficulty()}")
            print(f"  Questions: {len(quizz.get_questions())}")
            print(f"  Fill-ins: {len(quizz.get_fill_in_statements())}")
            print(f"  Minigames: {len(quizz.get_minigames())}")
            
            # Test get_quizz_task_count
            counts = service.get_quizz_task_count(quizz_id)
            print(f"  get_quizz_task_count({quizz_id}): {counts}")
            
            # Test get_exercises_as_frontend_format
            exercises = service.get_exercises_as_frontend_format(quizz)
            print(f"  get_exercises_as_frontend_format(): {len(exercises)} exercises")
            for ex in exercises[:3]:
                ex_type = ex.get('type')
                ex_content = ex.get('question', ex.get('image', ex.get('text', 'N/A')))
                if isinstance(ex_content, str) and len(ex_content) > 40:
                    ex_content = ex_content[:40] + "..."
                print(f"    - Type: {ex_type}, Content: {ex_content}")
    
    # NOTE: get_quizz_by_region_and_level, get_all_quizzes_for_region, get_level_count_for_region
    # require region_id/level_id columns in quizzes table which don't exist yet.
    print("\n--- Region/Level functions require region_id/level_id columns (skipped) ---")
    
    print(">--------------( QuizzService tests passed! )---------------<\n")
    return True


def test_quizz_task_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing QuizzTaskService )---------------<")
    
    task_repo = QuizzTaskRepository(con)
    question_repo = QuestionRepository(con)
    fill_in_repo = FillInStatementRepository(con)
    
    service = QuizzTaskService(task_repo, question_repo, fill_in_repo)
    
    # Test get_all_tasks
    all_tasks = service.get_all_tasks()
    print(f"get_all_tasks(): {len(all_tasks)} tasks found")
    
    # Test get_task_count_by_type
    counts = service.get_task_count_by_type()
    print(f"get_task_count_by_type(): {counts}")
    
    # Test get_tasks_by_quizz
    for quizz_id in [1, 2, 3]:
        quizz_tasks = service.get_tasks_by_quizz(quizz_id)
        print(f"get_tasks_by_quizz({quizz_id}): {len(quizz_tasks)} tasks")
    
    if all_tasks:
        task_id = all_tasks[0]['id']
        
        # Test get_task_type
        task_type = service.get_task_type(task_id)
        print(f"get_task_type({task_id}): {task_type}")
        
        # Test get_task_by_id
        full_task = service.get_task_by_id(task_id)
        if full_task:
            print(f"get_task_by_id({task_id}): {type(full_task).__name__}")
    
    print(">--------------( QuizzTaskService tests passed! )---------------<\n")
    return True


def test_region_service(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing RegionService )---------------<")
    
    repo = RegionRepository(con)
    service = RegionService(repo)
    
    # Test get_all_regions
    all_regions = service.get_all_regions()
    print(f"get_all_regions(): {len(all_regions)} regions found")
    
    for region_id, region_data in all_regions.items():
        print(f"  - ID {region_id}: {region_data.get('name')}")
    
    # Test get_region_by_id for each region found
    if all_regions:
        first_region_id = list(all_regions.keys())[0]
        region = service.get_region_by_id(first_region_id)
        if region:
            print(f"\nget_region_by_id({first_region_id}):")
            print(f"  Name: {region.get('name')}")
            print(f"  Mission: {region.get('mission')}")
            print(f"  Companion: {region.get('companion')}")
            print(f"  Description: {region.get('description')}")
    
    # Test get_region_by_name
    if all_regions:
        first_region_name = list(all_regions.values())[0].get('name')
        region_by_name = service.get_region_by_name(first_region_name)
        if region_by_name:
            print(f"\nget_region_by_name('{first_region_name}'): ID {region_by_name.get('id')}")
    
    print(">--------------( RegionService tests passed! )---------------<\n")
    return True


def test_game_service() -> bool:
    """Test GameService using the main database (read-only operations)."""
    print(">--------------( Testing GameService )---------------<")
    
    # Use the actual database path for GameService
    game = GameService(DB_PATH)
    
    # Test get_all_regions (replaces REGIONS_DATA)
    print("\n--- Testing REGIONS_DATA replacement ---")
    all_regions = game.get_all_regions()
    print(f"get_all_regions(): {len(all_regions)} regions")
    for region_id, data in all_regions.items():
        print(f"  Region {region_id}: {data.get('name')}")
    
    # Test get_region_data
    if all_regions:
        region_id = list(all_regions.keys())[0]
        region = game.get_region_data(region_id)
        print(f"\nget_region_data({region_id}): {region.get('name') if region else 'None'}")
    
    # NOTE: Functions that require region_id/level_id columns in quizzes table
    # are skipped: get_all_questions_data, get_exercises_for_level, 
    # get_user_progress, get_user_progress_for_region, is_level_unlocked
    print("\n--- Functions requiring region_id/level_id columns (skipped) ---")
    print("  - get_all_questions_data")
    print("  - get_exercises_for_level")
    print("  - get_user_progress")
    print("  - get_user_progress_for_region")
    print("  - is_level_unlocked")
    
    # Test service accessors
    print("\n--- Testing Service Accessors ---")
    print(f"game.region: {type(game.region).__name__}")
    print(f"game.quizz: {type(game.quizz).__name__}")
    print(f"game.player: {type(game.player).__name__}")
    print(f"game.question: {type(game.question).__name__}")
    print(f"game.fill_in: {type(game.fill_in).__name__}")
    print(f"game.minigame: {type(game.minigame).__name__}")
    
    # Test get_player_stats
    print("\n--- Testing Player Stats ---")
    stats = game.get_player_stats()
    if stats:
        print(f"get_player_stats(): name={stats.get('name')}, credits={stats.get('credits')}")
    else:
        print("get_player_stats(): No player found")
    
    # Test get_available_regions
    available = game.get_available_regions()
    print(f"get_available_regions(): {available}")
    
    game.close()
    
    print(">--------------( GameService tests passed! )---------------<\n")
    return True


# ==================== RUN TESTS ====================

def test_services() -> bool:
    """Run all service tests using existing database from domain."""
    print(f"Using database at: {DB_PATH}")
    
    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database not found at {DB_PATH}")
        return False
    
    con = get_database_connection()
    
    all_passed = True
    
    try:
        all_passed &= test_player_service(con)
        all_passed &= test_question_service(con)
        all_passed &= test_fill_in_service(con)
        all_passed &= test_minigame_service(con)
        all_passed &= test_quizz_service(con)
        all_passed &= test_quizz_task_service(con)
        all_passed &= test_region_service(con)
    except Exception as e:
        print(f"Error in service tests: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    finally:
        con.close()
    
    # GameService test
    try:
        all_passed &= test_game_service()
    except Exception as e:
        print(f"Error in GameService test: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    
    return all_passed


def run_tests() -> None:
    print(">--------------( Start service tests )---------------<\n")
    if test_services():
        print("\n>--------------( All service tests passed! )---------------<")
    else:
        print("\n>--------------( Some tests failed! )---------------<")


run_tests()
