from app.domain.interfaces.client_interface import IClientRepository
from app.models.client import Client


class ClientRepository(IClientRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Client).all()

    def get_by_id(self, client_id):
        return self.db.query(Client).filter(Client.id == client_id).first()

    def get_by_email_or_cpf(self, email, cpf):
        return self.db.query(Client).filter((Client.email == email) | (Client.cpf == cpf)).first()

    def create(self, client):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def update(self, db_client, update_data):
        for field, value in update_data.items():
            setattr(db_client, field, value)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def delete(self, db_client):
        self.db.delete(db_client)
        self.db.commit()
    
    def get_filtered(self, skip=0, limit=10, name=None, email=None):
        query = self.db.query(Client)
        if name:
            query = query.filter(Client.name.ilike(f"%{name}%"))
        if email:
            query = query.filter(Client.email.ilike(f"%{email}%"))
        return query.offset(skip).limit(limit).all()

