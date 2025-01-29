from backend.extensions.db import db

class ATSPicks(db.Model):
    __tablename__ = 'ATSPicks'  # Ensure this matches your actual table name if different

    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(45), nullable=False)
    away_team = db.Column(db.String(45), nullable=False)
    home_score = db.Column(db.Integer, nullable=True)  # Assuming scores can be nullable
    away_score = db.Column(db.Integer, nullable=True)
    pick = db.Column(db.String(45), nullable=False)
    probability = db.Column(db.Float, nullable=True)  # Assuming probability can be nullable
    season = db.Column(db.Integer, nullable=False)
    spread = db.Column(db.Float, nullable=False)
    week = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<ATSPicks {self.id} {self.home_team} vs {self.away_team}>'

