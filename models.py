from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PhoneNumber

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
	__tablename__ = 'Venue'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	city = db.Column(db.String(120))
	state = db.Column(db.String(120))
	address = db.Column(db.String(120))

	phone_number = db.Column(db.Unicode(255))
	phone_country_code = db.Column(db.Unicode(8))
	phone = db.composite(PhoneNumber, phone_number, phone_country_code)
	
	image_link = db.Column(db.String(500))
	facebook_link = db.Column(db.String(120))
	
	# TODO: implement any missing fields, as a database migration using Flask-Migrate
	website_link = db.Column(db.String(120))
	genres = db.Column(db.ARRAY(db.String))
	seeking_talent = db.Column(db.Boolean)
	seeking_description = db.Column(db.String(500))
	shows = db.relationship('Show', backref='venue', lazy=True, cascade='all, delete', passive_deletes=True)
	
	def __repr__(self):
		return f'<Venue ID: {self.id}, Name: {self.name}, City: {self.city}, State: {self.state}, Address: {self.address}, Phone: {self.phone}, Image link: {self.image_link}, Facebook link: {self.facebook_link}, Website link: {self.website_link}, Genre: {self.genres}, Seeking talent: {self.seeking_talent}, Seeking description: {self.seeking_description}>'
		
class Artist(db.Model):
	__tablename__ = 'Artist'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	city = db.Column(db.String(120))
	state = db.Column(db.String(120))
	
	phone_number = db.Column(db.Unicode(255))
	phone_country_code = db.Column(db.Unicode(8))
	phone = db.composite(PhoneNumber, phone_number, phone_country_code)
	
	genres = db.Column(db.ARRAY(db.String))
	availability = db.Column(db.ARRAY(db.String))
	image_link = db.Column(db.String(500))
	facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using Flask-Migrate
	website_link = db.Column(db.String(120))
	seeking_venue = db.Column(db.Boolean)
	seeking_description = db.Column(db.String(500))
	
	shows = db.relationship('Show', backref='artist', lazy=True, cascade='all, delete', passive_deletes=True)

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__ = 'Show'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime(), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='CASCADE'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='CASCADE'), nullable=False)

  def __repr__(self):
    return f'<Show ID: {self.id}, Start time: {self.start_time}, Artist ID: {self.artist_id}, Venue ID: {self.venue_id}>'
