import pytest
from datetime import date, timedelta
from habit_logic import Habit, HabitTracker

TODAY = date(2025, 6, 9)
YESTERDAY = TODAY - timedelta(days=1)
DAY_BEFORE = YESTERDAY - timedelta(days=1)

def test_add_new_habit():
    """Testa a criação básica de um hábito"""
    tracker = HabitTracker()
    assert tracker.add_habit("Ler livro")
    assert len(tracker.habits) == 1
    assert tracker.habits[0].name == "Ler livro"

def test_add_duplicate_habit_fails():
    """Verifica que não é possível adicionar hábitos duplicados"""
    tracker = HabitTracker()
    tracker.add_habit("Beber água")
    assert not tracker.add_habit("Beber água")
    assert len(tracker.habits) == 1

def test_delete_habit():
    """Testa a remoção de um hábito existente"""
    tracker = HabitTracker()
    tracker.add_habit("Correr")
    tracker.delete_habit("Correr")
    assert len(tracker.habits) == 0

def test_mark_habit_complete():
    """Verifica a marcação de hábito como completo"""
    tracker = HabitTracker()
    tracker.add_habit("Estudar")
    tracker.mark_complete("Estudar", TODAY)
    assert tracker.is_complete_today("Estudar", TODAY)

def test_correctly_calculates_streak_of_three_when_done_today():
    """Testa o cálculo de sequência (streak) corretamente"""
    tracker = HabitTracker()
    tracker.add_habit("Caminhar")
    tracker.mark_complete("Caminhar", TODAY)
    tracker.mark_complete("Caminhar", YESTERDAY)
    tracker.mark_complete("Caminhar", DAY_BEFORE)
    assert tracker.get_current_streak("Caminhar", TODAY) == 3