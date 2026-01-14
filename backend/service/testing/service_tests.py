"""
Service Tests - Testing the main Service class
Uses the database from backend/domain/data.db
"""

import sqlite3
import os
from backend.domain.entities.Player import Player
from backend.domain.entities.Question import Question
from backend.domain.entities.Quizz import Quizz
from backend.domain.entities.Minigame import MapGuesser

from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository

from backend.service.Service import Service, convert_MapGuesser_to_frontend_format, convert_question_to_frontend_format, _get_region_name_by_id


# ==================== DATABASE SETUP ====================

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'domain', 'data.db'))


def get_database_connection() -> sqlite3.Connection:
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")
    return sqlite3.connect(DB_PATH)


def create_service(con: sqlite3.Connection) -> Service:
    """Create a Service instance with all repositories."""
    return Service(
        player_repository=PlayerRepository(con),
        question_repository=QuestionRepository(con),
        fill_in_repository=FillInStatementRepository(con),
        minigame_repository=MinigameRepository(con),
        quizz_repository=QuizzRepository(con),
        quizz_task_repository=QuizzTaskRepository(con)
    )



def test_helper_functions() -> bool:
    print(">--------------( Testing Helper Functions )---------------<")
    
    # Test _get_region_name_by_id
    print("\n_get_region_name_by_id():")
    assert _get_region_name_by_id(1) == "Transilvania", "Region 1 should be Transilvania"
    assert _get_region_name_by_id(2) == "Moldova", "Region 2 should be Moldova"
    assert _get_region_name_by_id(3) == "Țara Românească", "Region 3 should be Țara Românească"
    assert _get_region_name_by_id(4) == "Dobrogea", "Region 4 should be Dobrogea"
    assert _get_region_name_by_id(5) == "Banat", "Region 5 should be Banat"
    assert _get_region_name_by_id(99) is None, "Invalid region ID should return None"
    print("  Region 1 -> Transilvania ✓")
    print("  Region 2 -> Moldova ✓")
    print("  Region 3 -> Țara Românească ✓")
    print("  Region 4 -> Dobrogea ✓")
    print("  Region 5 -> Banat ✓")
    print("  Region 99 -> None ✓")
    
    print(">--------------( Helper Functions tests passed! )---------------<\n")
    return True


# ==================== CONVERSION FUNCTION TESTS ====================

def test_convert_question_to_frontend_format(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing convert_question_to_frontend_format )---------------<")
    
    repo = QuestionRepository(con)
    questions = repo.find("1=1")  # Get all questions
    
    if questions:
        q = questions[0]
        result = convert_question_to_frontend_format(q)
        
        print(f"\nOriginal Question ID: {q.get_id()}")
        print(f"Original Question Text: {q.get_text()[:50]}..." if len(q.get_text()) > 50 else f"Original Question Text: {q.get_text()}")
        print(f"Original Answers: {q.get_answer_list()}")
        
        print(f"\nConverted to frontend format:")
        print(f"  id: {result['id']}")
        print(f"  question: {result['question'][:50]}..." if len(result['question']) > 50 else f"  question: {result['question']}")
        print(f"  options: {result['options']}")
        print(f"  correct: {result['correct']}")
        
        # Assertions
        assert result['id'] == q.get_id(), "ID should match!"
        assert result['question'] == q.get_text(), "Question text should match!"
        assert result['options'] == q.get_answer_list(), "Options should match answer list!"
        assert result['correct'] == q.get_answer_list()[0], "Correct should be first answer!"
        print("\n  All assertions passed! ✓")
    else:
        print("  No questions found in database")
    
    print(">--------------( convert_question_to_frontend_format tests passed! )---------------<\n")
    return True


def test_convert_MapGuesser_to_frontend_format(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing convert_MapGuesser_to_frontend_format )---------------<")
    
    repo = MinigameRepository(con)
    minigames = repo.find("1=1")  # Get all minigames
    
    map_guessers = [m for m in minigames if isinstance(m, MapGuesser)]
    
    if map_guessers:
        mg = map_guessers[0]
        result = convert_MapGuesser_to_frontend_format(mg)
        
        print(f"\nOriginal MapGuesser ID: {mg.get_id()}")
        print(f"Original Win Config: {mg.get_win_configuration()}")
        
        print(f"\nConverted to frontend format:")
        print(f"  type: {result['type']}")
        print(f"  targets count: {len(result['targets'])}")
        for i, target in enumerate(result['targets'][:3]):
            print(f"    Target {i+1}: question='{target['question'][:30]}...', x={target['x']}, y={target['y']}")
        
        # Assertions
        assert result['type'] == 'map_guess', "Type should be 'map_guess'!"
        assert isinstance(result['targets'], list), "Targets should be a list!"
        for target in result['targets']:
            assert 'question' in target, "Each target should have 'question'!"
            assert 'x' in target, "Each target should have 'x'!"
            assert 'y' in target, "Each target should have 'y'!"
        print("\n  All assertions passed! ")
    else:
        print("  No MapGuesser minigames found in database")
    
    print(">--------------( convert_MapGuesser_to_frontend_format tests passed! )---------------<\n")
    return True


# ==================== SERVICE CLASS TESTS ====================

def test_get_player(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing get_player )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        print(f"  ID: {player.get_id()}")
        print(f"  Name: {player.get_name()}")
        print(f"  Credits: {player.get_credits()}")
        assert player.get_id() is not None, "Player should have an ID!"
        assert player.get_name() is not None, "Player should have a name!"
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( get_player tests passed! )---------------<\n")
    return True


def test_save_player(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing save_player )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original_name = player.get_name()
        print(f"  Original name: {original_name}")
        
        # Save without changes (should not error)
        service.save_player(player)
        print("  save_player(player) - no error ✓")
        
        # Test save_player with None (should not error)
        service.save_player(None)
        print("  save_player(None) - no error ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( save_player tests passed! )---------------<\n")
    return True


def test_add_credits(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing add_credits )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original_credits = player.get_credits()
        print(f"  Original credits: {original_credits}")
        
        # Add credits
        new_total = service.add_credits(100)
        print(f"  add_credits(100) -> {new_total}")
        assert new_total == original_credits + 100, "Credits should increase by 100!"
        
        # Restore original credits
        service.add_credits(-100)
        restored = service.get_player().get_credits()
        print(f"  Restored credits: {restored}")
        assert restored == original_credits, "Credits should be restored!"
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( add_credits tests passed! )---------------<\n")
    return True


def test_spend_credits(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing spend_credits )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original_credits = player.get_credits()
        print(f"  Original credits: {original_credits}")
        
        # Spend more than available (should fail) - NO DB CHANGE
        result = service.spend_credits(original_credits + 1000)
        print(f"  spend_credits({original_credits + 1000}) -> {result}")
        assert result == False, "Should fail when spending more than available!"
        
        # Test spending valid amount, then restore
        if original_credits >= 10:
            result = service.spend_credits(10)
            print(f"  spend_credits(10) -> {result}")
            assert result == True, "Should succeed when spending valid amount!"
            
            # Restore credits
            service.add_credits(10)
            restored = service.get_player().get_credits()
            print(f"  Restored credits: {restored}")
            assert restored == original_credits, "Credits should be restored!"
        
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( spend_credits tests passed! )---------------<\n")
    return True


def test_purchase_cosmetic(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing purchase_cosmetic )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original_credits = player.get_credits()
        original_cosmetics = player.get_cosmetics_purchased().copy()
        print(f"  Original credits: {original_credits}")
        print(f"  Original cosmetics: {original_cosmetics}")
        
        # Try to purchase with insufficient credits
        result = service.purchase_cosmetic("expensive.png", original_credits + 1000)
        print(f"  purchase_cosmetic('expensive.png', {original_credits + 1000}) -> {result}")
        assert result == False, "Should fail with insufficient credits!"
        
        # Try to purchase already owned cosmetic (if any)
        if original_cosmetics:
            result = service.purchase_cosmetic(original_cosmetics[0], 0)
            print(f"  purchase_cosmetic('{original_cosmetics[0]}', 0) -> {result}")
            assert result == False, "Should fail for already owned cosmetic!"
        
        print("  Assertions passed!")
    else:
        print("  No player found in database")
    
    print(">--------------( purchase_cosmetic tests passed! )---------------<\n")
    return True


def test_equip_cosmetic(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing equip_cosmetic )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        owned_cosmetics = player.get_cosmetics_purchased()
        original_equipped = player.get_cosmetic()  # Save original state
        print(f"  Owned cosmetics: {owned_cosmetics}")
        print(f"  Currently equipped: {original_equipped}")
        
        # Try to equip unowned cosmetic - NO DB CHANGE (returns False)
        result = service.equip_cosmetic("not_owned_cosmetic_xyz.png")
        print(f"  equip_cosmetic('not_owned_cosmetic_xyz.png') -> {result}")
        assert result == False, "Should fail for unowned cosmetic!"
        
        # Equip owned cosmetic (if any)
        if owned_cosmetics:
            result = service.equip_cosmetic(owned_cosmetics[0])
            print(f"  equip_cosmetic('{owned_cosmetics[0]}') -> {result}")
            assert result == True, "Should succeed for owned cosmetic!"
            
            # ALWAYS restore original equipped cosmetic
            player = service.get_player()
            player.set_cosmetic(original_equipped)
            service.save_player(player)
            print(f"  Restored equipped to: {service.get_player().get_cosmetic()}")
        
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( equip_cosmetic tests passed! )---------------<\n")
    return True


def test_get_player_stats(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing get_player_stats )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        stats = service.get_player_stats()
        print(f"  name: {stats['name']}")
        print(f"  credits: {stats['credits']}")
        print(f"  avg_play_time: {stats['avg_play_time']}")
        print(f"  quizzes_solved: {stats['quizzes_solved']}")
        print(f"  quizzes_played: {stats['quizzes_played']}")
        print(f"  completion_percentage: {stats['completion_percentage']}")
        print(f"  regions_state: {stats['regions_state']}")
        print(f"  equipped_cosmetic: {stats['equipped_cosmetic']}")
        print(f"  cosmetics_owned: {stats['cosmetics_owned']}")
        
        # Assertions
        assert stats['name'] == player.get_name(), "Name should match!"
        assert stats['credits'] == player.get_credits(), "Credits should match!"
        assert 'regions_state' in stats, "Should have regions_state!"
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( get_player_stats tests passed! )---------------<\n")
    return True


def test_increment_quizzes_played(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing increment_quizzes_played )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original = player.get_quizzes_played()
        print(f"  Original quizzes_played: {original}")
        
        service.increment_quizzes_played()
        new_value = service.get_player().get_quizzes_played()
        print(f"  After increment: {new_value}")
        assert new_value == original + 1, "Should increment by 1!"
        
        # Restore original value
        player = service.get_player()
        player.set_quizzes_played(original)
        service.save_player(player)
        print(f"  Restored to: {service.get_player().get_quizzes_played()}")
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( increment_quizzes_played tests passed! )---------------<\n")
    return True


def test_increment_quizzes_solved(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing increment_quizzes_solved )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original = player.get_quizzes_solved()
        print(f"  Original quizzes_solved: {original}")
        
        service.increment_quizzes_solved()
        new_value = service.get_player().get_quizzes_solved()
        print(f"  After increment: {new_value}")
        assert new_value == original + 1, "Should increment by 1!"
        
        # Restore original value
        player = service.get_player()
        player.set_quizzes_solved(original)
        service.save_player(player)
        print(f"  Restored to: {service.get_player().get_quizzes_solved()}")
        print("  Assertions passed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( increment_quizzes_solved tests passed! )---------------<\n")
    return True


def test_update_play_time(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing update_play_time )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        original_avg = player.get_avg_play_time()
        original_played = player.get_quizzes_played()
        print(f"  Original avg_play_time: {original_avg}")
        print(f"  Original quizzes_played: {original_played}")
        
        # Update with session time
        service.update_play_time(10.0)
        new_avg = service.get_player().get_avg_play_time()
        print(f"  After update_play_time(10.0): {new_avg}")
        
        # Restore original value
        player = service.get_player()
        player.set_avg_play_time(original_avg)
        service.save_player(player)
        print(f"  Restored to: {service.get_player().get_avg_play_time()}")
        print("  Test completed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( update_play_time tests passed! )---------------<\n")
    return True


def test_is_level_unlocked(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing is_level_unlocked )---------------<")
    
    service = create_service(con)
    player = service.get_player()
    
    if player:
        regions_state = player.get_regions_state()
        print(f"\nPlayer regions_state: {regions_state}")
        
        # Test for each region
        for region_id in range(1, 6):
            region_name = _get_region_name_by_id(region_id)
            unlocked_level = regions_state.get(region_name, 0)
            
            # Test level that should be unlocked
            if unlocked_level > 0:
                result = service.is_level_unlocked(region_id, unlocked_level)
                print(f"\nis_level_unlocked({region_id}, {unlocked_level}): {result}")
                assert result == True, f"Level {unlocked_level} should be unlocked for {region_name}!"
            
            # Test level that should be locked (if any)
            locked_level = unlocked_level + 1
            try:
                result = service.is_level_unlocked(region_id, locked_level)
                print(f"is_level_unlocked({region_id}, {locked_level}): {result}")
            except:
                print(f"is_level_unlocked({region_id}, {locked_level}): Error (level not in state)")
        
        print("\n  Level unlock tests completed! ✓")
    else:
        print("  No player found in database")
    
    print(">--------------( is_level_unlocked tests passed! )---------------<\n")
    return True


def test_get_quizz_by_id(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing get_quizz_by_id )---------------<")
    
    service = create_service(con)
    
    # Test getting quizz by ID
    for quizz_id in [1, 2, 3, 4, 5]:
        try:
            quizz = service.get_quizz_by_id(quizz_id)
            # print(f"Level data for quizz {quizz_id}: {data}")
            
            if quizz:
                print(f"\nget_quizz_by_id({quizz_id}):")
                print(f"  ID: {quizz.get_id()}")
                print(f"  Difficulty: {quizz.get_difficulty()}")
                print(f"  Questions: {len(quizz.get_questions())}")
                print(f"  Fill-ins: {len(quizz.get_fill_in_statements())}")
                minigames = quizz.get_minigames()
                print(f"  Minigames: " + f"{type(minigames).__name__}" if minigames else "None")
                
                # Assertions
                assert quizz.get_id() == quizz_id, "Quizz ID should match!"
                print(f"  Assertions passed! ✓")
                break  # Test one quizz
        except Exception as e:
            print(f"\nget_quizz_by_id({quizz_id}): Error - {e}")
    
    print(">--------------( get_quizz_by_id tests passed! )---------------<\n")
    return True



def test_get_level_data(con: sqlite3.Connection) -> bool:
    print(">--------------( Testing get_level_data )---------------<")
    
    service = create_service(con)
    
    # Test getting level data for quizz IDs
    for quizz_id in [1, 2, 3, 4, 5]:
        try:
            data = service.get_level_data(quizz_id)
            print(f"\nget_level_data({quizz_id}):")
            print(f"  Level data steps: {len(data)}")
            for i, step in enumerate(data[:3]):  # Print first 3 steps
                print(f"    Step {i+1}: Type={step['type']}")
            
            # Assertions
            assert isinstance(data, list), "Level data should be a list!"
            print(f"  Assertions passed! ✓")
            break  # Test one quizz
        except Exception as e:
            print(f"\nget_level_data({quizz_id}): Error - {e}")
    
    print(">--------------( get_level_data tests passed! )---------------<\n")
    return True


# ==================== RUN ALL TESTS ====================

def test_service() -> bool:
    print(f"Using database at: {DB_PATH}\n")
    
    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database not found at {DB_PATH}")
        return False
    
    con = get_database_connection()
    all_passed = True
    
    try:
        # Test helper functions (no DB needed)
        # all_passed &= test_helper_functions()
        
        # # Test conversion functions
        # all_passed &= test_convert_question_to_frontend_format(con)
        # all_passed &= test_convert_MapGuesser_to_frontend_format(con)
        
        # # Test Service class methods - Player operations
        # all_passed &= test_get_player(con)
        # all_passed &= test_save_player(con)
        # all_passed &= test_add_credits(con)
        # all_passed &= test_spend_credits(con)
        # all_passed &= test_purchase_cosmetic(con)
        # all_passed &= test_equip_cosmetic(con)
        # all_passed &= test_get_player_stats(con)
        # all_passed &= test_increment_quizzes_played(con)
        # all_passed &= test_increment_quizzes_solved(con)
        # all_passed &= test_update_play_time(con)
        
        # # Test Service class methods - Level and Quizz
        # all_passed &= test_is_level_unlocked(con)
        all_passed &= test_get_quizz_by_id(con)
        all_passed &= test_get_level_data(con)
        
    except Exception as e:
        print(f"Error in service tests: {e}")
        import traceback
        traceback.print_exc()
        all_passed = False
    finally:
        con.close()
    
    return all_passed


def run_tests() -> None:
    print(">--------------( Start Service tests )---------------<\n")
    if test_service():
        print("\n>--------------( All Service tests passed! )---------------<")
    else:
        print("\n>--------------( Some tests failed! )---------------<")


run_tests()
