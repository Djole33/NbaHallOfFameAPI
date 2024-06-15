from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample data of Hall of Fame players with their points
hall_of_fame_players = [
    {"id": 1, "name": "Kareem Abdul-Jabbar", "points": 38387},
    {"id": 2, "name": "Karl Malone", "points": 36928},
    {"id": 3, "name": "Kobe Bryant", "points": 33643},
    {"id": 4, "name": "Michael Jordan", "points": 32292},
    {"id": 5, "name": "Dirk Nowitzki", "points": 31560},
    {"id": 6, "name": "Wilt Chamberlain", "points": 31419},
    {"id": 7, "name": "Shaquille O'Neal", "points": 28596},
    {"id": 8, "name": "Moses Malone", "points": 27409},
    {"id": 9, "name": "Elvin Hayes", "points": 27313},
    {"id": 10, "name": "Hakeem Olajuwon", "points": 26946},
    {"id": 11, "name": "Oscar Robertson", "points": 26710},
    {"id": 12, "name": "Dominique Wilkins", "points": 26668},
    {"id": 13, "name": "Tim Duncan", "points": 26496},
    {"id": 14, "name": "Paul Pierce", "points": 26397},
    {"id": 15, "name": "John Havlicek", "points": 26395},
    {"id": 16, "name": "Kevin Garnett", "points": 26071},
    {"id": 17, "name": "Alex English", "points": 25613},
    {"id": 18, "name": "Reggie Miller", "points": 25279},
    {"id": 19, "name": "Jerry West", "points": 25192},
    {"id": 20, "name": "Patrick Ewing", "points": 24815},
    {"id": 21, "name": "Allen Iverson", "points": 24368},
    {"id": 22, "name": "Charles Barkley", "points": 23757},
    {"id": 23, "name": "Robert Parish", "points": 23334},
    {"id": 24, "name": "Adrian Dantley", "points": 23177},
    {"id": 25, "name": "Ray Allen", "points": 24505},
    {"id": 26, "name": "George Gervin", "points": 20708},
    {"id": 27, "name": "Scottie Pippen", "points": 18940},
    {"id": 28, "name": "David Robinson", "points": 20790},
    {"id": 29, "name": "Clyde Drexler", "points": 22195},
    {"id": 30, "name": "Gary Payton", "points": 21813},
    {"id": 31, "name": "Larry Bird", "points": 21791},
    {"id": 32, "name": "Hal Greer", "points": 21586},
    {"id": 33, "name": "Bob Pettit", "points": 20880},
    {"id": 34, "name": "Elgin Baylor", "points": 23149},
    {"id": 35, "name": "James Worthy", "points": 16320},
    {"id": 36, "name": "Isiah Thomas", "points": 18822},
    {"id": 37, "name": "John Stockton", "points": 19711},
    {"id": 38, "name": "Rick Barry", "points": 18395},
    {"id": 39, "name": "Bernard King", "points": 19655},
    {"id": 40, "name": "Bob Cousy", "points": 16960},
    {"id": 41, "name": "Bill Russell", "points": 14522},
    {"id": 42, "name": "Walt Frazier", "points": 15211},
    {"id": 43, "name": "Chris Mullin", "points": 17911},
    {"id": 44, "name": "Alonzo Mourning", "points": 14911},
    {"id": 45, "name": "Nate Thurmond", "points": 14937},
    {"id": 46, "name": "Arvydas Sabonis", "points": 11674},
    {"id": 47, "name": "Pete Maravich", "points": 15948},
    {"id": 48, "name": "Julius Erving", "points": 30026},
    {"id": 49, "name": "Bill Walton", "points": 6215},
    {"id": 50, "name": "George Mikan", "points": 10156},
    {"id": 51, "name": "David Thompson", "points": 11934},
    {"id": 52, "name": "Mitch Richmond", "points": 20497},
    {"id": 53, "name": "Dražen Petrović", "points": 4398},
    {"id": 54, "name": "Spencer Haywood", "points": 14592},
    {"id": 55, "name": "Dennis Rodman", "points": 6683},
    {"id": 56, "name": "Ralph Sampson", "points": 7039},
    {"id": 57, "name": "Manu Ginóbili", "points": 14043},
    {"id": 58, "name": "Grant Hill", "points": 17137},
    {"id": 59, "name": "Jason Kidd", "points": 17529},
    {"id": 60, "name": "Steve Nash", "points": 17387},
    {"id": 61, "name": "Chris Webber", "points": 17182}
]

# Endpoint to fetch all players
@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(hall_of_fame_players)

# Endpoint to fetch a specific player by their ID
@app.route('/player/<int:id>', methods=['GET'])
def get_player(id):
    # Attempt to find the player with the given ID
    player = next((player for player in hall_of_fame_players if player["id"] == id), None)
    if player is not None:
        return jsonify(player)
    else:
        return jsonify({"error": "Player not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run()

