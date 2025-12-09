import sqlite3
from typing import Optional

from backend.domain.entities.Player import Player


class PlayerRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TABLE = "player"

    def save(self, player: Player) -> None:
        stats = player.get_statistics()

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (player.get_id(),))
        exists = self.cursor.fetchone()

        regions_unlocked = '|'.join(stats['regions_unlocked'])
        cosmetics_unlocked = '|'.join(stats['cosmetics_unlocked'])
        cosmetics_purchased = '|'.join(stats['cosmetics_purchased'])

        if exists:
            sql = f"""
                UPDATE {self.TABLE} 
                SET name = ?, credits = ?, avg_play_time = ?, quizzes_solved = ?, 
                    quizzes_played = ?, regions_unlocked = ?, cosmetics_unlocked = ?, 
                    cosmetics_purchased = ?, completion_percentage = ?
                WHERE id = ?
            """
            self.cursor.execute(sql, (
                player.get_name(), player.get_credits(),
                stats['avg_play_time'], stats['quizzes_solved'], stats['quizzes_played'],
                regions_unlocked, cosmetics_unlocked, cosmetics_purchased,
                stats['completion_percentage'], player.get_id()
            ))
        else:
            sql = f"""
                INSERT INTO {self.TABLE} (name, credits, avg_play_time, quizzes_solved, quizzes_played, regions_unlocked, cosmetics_unlocked, cosmetics_purchased, completion_percentage) 
                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(sql, (
                player.get_name(), player.get_credits(),
                stats['avg_play_time'], stats['quizzes_solved'], stats['quizzes_played'],
                regions_unlocked, cosmetics_unlocked, cosmetics_purchased,
                stats['completion_percentage']
            ))

        self.conn.commit()

    def get_player_id_by_name(self, name: str) -> Optional[int]:
        sql = f"""
            SELECT id FROM {self.TABLE} WHERE name = ?
        """
        self.cursor.execute(sql, (name,))
        row = self.cursor.fetchone()
        if row:
            return row[0]
        return None

    def get(self) -> Optional[object]:
        self.cursor.execute(f"SELECT * FROM {self.TABLE} LIMIT 1")
        row = self.cursor.fetchone()

        if row:
            player = Player(row[0], row[1])
            player.set_credits(row[2])
            player.set_cosmetic(row[11])
            player.set_avg_play_time(row[3])
            player.set_quizzes_solved(row[4])
            player.set_quizzes_played(row[5])
            player.set_regions_unlocked(row[6].split('|') if row[6] else [])
            player.set_cosmetics_unlocked(row[7].split('|') if row[7] else [])
            player.set_cosmetics_purchased(row[8].split('|') if row[8] else [])
            player.set_completion_percentage(row[9])

            return player
        return None

    def get_by_id(self, player_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT * FROM {self.TABLE} WHERE id = ?", (player_id,))
        row = self.cursor.fetchone()

        if row:
            player = Player(row[0], row[1])
            player.set_credits(row[2])
            player.set_cosmetic(row[11])
            player.set_avg_play_time(row[3])
            player.set_quizzes_solved(row[4])
            player.set_quizzes_played(row[5])
            player.set_regions_unlocked(row[6].split('|') if row[6] else [])
            player.set_cosmetics_unlocked(row[7].split('|') if row[7] else [])
            player.set_cosmetics_purchased(row[8].split('|') if row[8] else [])
            player.set_completion_percentage(row[9])

            return player
        return None

    def get_all(self) -> list[Player]:
        self.cursor.execute(f"SELECT * FROM {self.TABLE}")
        rows = self.cursor.fetchall()
        players = []
        for row in rows:
            player = Player(row[0], row[1])
            player.set_credits(row[2])
            player.set_cosmetic(row[11])
            player.set_avg_play_time(row[3])
            player.set_quizzes_solved(row[4])
            player.set_quizzes_played(row[5])
            player.set_regions_unlocked(row[6].split('|') if row[6] else [])
            player.set_cosmetics_unlocked(row[7].split('|') if row[7] else [])
            player.set_cosmetics_purchased(row[8].split('|') if row[8] else [])
            player.set_completion_percentage(row[9])
            players.append(player)
        return players

    def delete(self, player_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (player_id,))
        self.conn.commit()
