import sqlite3
from typing import Optional
from backend.domain.entities.Player import Player

class PlayerRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.TABLE = "player"
        self.REGIONS_TABLE = "regions"

    def save(self, player: Player) -> None:
        stats = player.get_statistics()
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (player.get_id(),))
            cosmetics_purchased = '|'.join(stats['cosmetics_purchased'])

            if cursor.fetchone():
                sql = f"""
                    UPDATE {self.TABLE} 
                    SET name = ?, credits = ?, avg_play_time = ?, quizzes_solved = ?, quizzes_played = ?,
                        cosmetics_purchased = ?, completion_percentage = ?, equipped_cosmetic = ? WHERE id = ?
                    """
                cursor.execute(sql, (
                    player.get_name(), player.get_credits(), stats['avg_play_time'],
                    stats['quizzes_solved'], stats['quizzes_played'], cosmetics_purchased,
                    stats['completion_percentage'], player.get_cosmetic(), player.get_id()
                ))
                for region, state in stats['regions_state'].items():
                    cursor.execute(f"UPDATE {self.REGIONS_TABLE} SET state = ? WHERE name = ?", (state, region))
            else:
                sql = f"""
                    INSERT INTO {self.TABLE} (name, credits, avg_play_time, quizzes_solved, quizzes_played, cosmetics_purchased, completion_percentage) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """
                cursor.execute(sql, (
                    player.get_name(), player.get_credits(), stats['avg_play_time'], stats['quizzes_solved'],
                    stats['quizzes_played'], cosmetics_purchased, stats['completion_percentage']
                ))

            self.conn.commit()
        except sqlite3.Error as e: self.conn.rollback(); print(e)

    def get(self) -> Optional[Player]:
        self.conn.row_factory = sqlite3.Row  # Access columns by name
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.TABLE} LIMIT 1")
        row = cursor.fetchone()
        if row:
            player = Player(row['id'], row['name'])
            player.set_credits(row['credits'])
            player.set_avg_play_time(row['avg_play_time'])
            player.set_quizzes_solved(row['quizzes_solved'])
            player.set_quizzes_played(row['quizzes_played'])
            player.set_cosmetics_purchased(row['cosmetics_purchased'].split('|') if row['cosmetics_purchased'] else [])
            player.set_completion_percentage(row['completion_percentage'])
            player.set_cosmetic(row['equipped_cosmetic'])

            cursor.execute(f"SELECT name, state FROM {self.REGIONS_TABLE}")
            player.set_regions_state({r['name']: r['state'] for r in cursor.fetchall()})
            return player
        return None

    def delete(self, player_id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (player_id,))
        cursor.execute("DELETE FROM sqlite_sequence WHERE name=?", ("player",))
        for region_id in range(1, 6): cursor.execute(f"UPDATE {self.REGIONS_TABLE} SET state = 1 WHERE id = {region_id}")
        self.conn.commit()