import sqlite3
import json
from typing import Optional
from backend.domain.entities.Player import Player # Presupus import

class PlayerRepository:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.TABLE = "Player"

    def save(self, player: Player) -> None:
        stats_json = json.dumps(player.get_statistics())

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (player.get_id(),))
        exists = self.cursor.fetchone()

        if exists:
            sql = f"""
                UPDATE {self.TABLE} 
                SET name = ?, credits = ?, cosmetic = ?, statistics = ? 
                WHERE id = ?
            """
            self.cursor.execute(sql, (player.get_name(), player.get_credits(), player.get_cosmetic(), stats_json,
                                      player.get_id()))
        else:
            sql = f"""
                INSERT INTO {self.TABLE} (id, name, credits, cosmetic, statistics) 
                VALUES (?, ?, ?, ?, ?)
            """
            self.cursor.execute(sql, (player.get_id(), player.get_name(), player.get_credits(), player.get_cosmetic(),
                                      stats_json))

        self.conn.commit()

    def get(self) -> Optional[Player]:
        self.cursor.execute(f"SELECT id, name, credits, cosmetic, statistics FROM {self.TABLE} LIMIT 1")
        row = self.cursor.fetchone()

        if row:
            stats_dict = json.loads(row[4])
            player = Player(row[0], row[1])
            player.set_credits(row[2])
            player.set_cosmetic(row[3])
            player._Player__statistics = stats_dict
            return player
        return None

    def delete(self, player_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (player_id,))

        if self.cursor.rowcount == 0:
            raise KeyError(f"No Player exists with ID {player_id} for deletion.")

        self.conn.commit()