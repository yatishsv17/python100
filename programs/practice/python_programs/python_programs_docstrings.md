# Python Programs Documentation

This document contains all Python file names and their essential documentation, consolidated from simple and production versions.

---

## 1_band_name_generator.py

**Description:** Generates a creative band name by combining the user's city name with their pet's name in various formats.

**Inputs:**
- City name: The city where the user grew up (string, alphabetic characters only)
- Pet's name: The name of the user's pet (string, alphabetic characters only)

**Outputs:**
- Generated band name in various formats (e.g., "The {city} {pet}", "The {pet} {city}")
- Style information indicating which format was used
- Error messages for invalid inputs

**Rules:**
- Both inputs must be non-empty and at least 2 characters
- Multiple band name styles available (Classic, Reversed, With Of, Modern)
- Input validation with retry logic

**Assumptions:**
- User provides English alphabetic inputs
- City and pet names are real and meaningful
- Band names should be properly capitalized

---

## 2_tip_calculator.py

**Description:** Calculates how much each person should pay when splitting a bill including a tip. The user enters the total bill amount, tip percentage, and number of people.

**Inputs:**
- Total bill amount: Float greater than 0
- Tip percentage: Integer (10, 12, or 15)
- Number of people: Integer greater than 0

**Outputs:**
- Amount each person should pay (formatted to 2 decimal places)
- Detailed breakdown of calculation steps
- Warning messages for unusual values
- Error messages for invalid inputs

**Rules:**
- Bill must be greater than 0
- Tip percentage must be exactly 10, 12, or 15
- Number of people must be greater than 0
- Equal split among all people

**Assumptions:**
- User wants to split bill equally among all people
- Tip percentages are limited to 10%, 12%, or 15%
- Currency is in dollars (or equivalent decimal currency)
- All people pay the same amount

---

## 3_treasure_island.py

**Description:** A text-based adventure game where the player navigates through a series of choices to find the treasure on Treasure Island. Wrong choices lead to game over, while the correct path leads to victory.

**Inputs:**
- First choice: 'left' or 'right' (case-insensitive)
- Second choice: 'wait' or 'swim' (case-insensitive)
- Third choice: 'red', 'yellow', or 'blue' (case-insensitive)

**Outputs:**
- Scenario descriptions for each choice point
- Game over messages with cause of death
- Victory message when treasure is found
- Error messages for invalid inputs

**Rules:**
- Winning path: left → wait → yellow door
- Wrong choices lead to immediate game over
- Case-insensitive input handling

**Assumptions:**
- User understands the adventure game concept
- Choices are based on the provided flowchart
- Simple text-based interface is sufficient
- Single playthrough per execution

---

## 4_rock_paper_scissors.py

**Description:** The classic Rock Paper Scissors game where the user plays against the computer. The computer randomly selects its choice, and the winner is determined based on standard game rules.

**Inputs:**
- User choice: 'rock', 'paper', or 'scissors' (case-insensitive)

**Outputs:**
- User's choice with emoji
- Computer's choice with emoji
- Game result (you win/computer wins/it's a tie)
- Error messages for invalid inputs

**Rules:**
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choice = Tie

**Assumptions:**
- User understands Rock Paper Scissors rules
- Single round per execution
- Computer choice is truly random
- Standard game rules apply

---

## 5_password_generator.py

**Description:** Generates secure random passwords based on user specifications for the number of letters, symbols, and numbers. The password is shuffled to randomize character order.

**Inputs:**
- Number of letters: Integer >= 0 (a-z, A-Z)
- Number of symbols: Integer >= 0 (!@#$%^&*()_+-=[]{}|;:,.<>?)
- Number of numbers: Integer >= 0 (0-9)

**Outputs:**
- Generated password string
- Password composition breakdown
- Password length information
- Security recommendations
- Error messages for invalid inputs

**Rules:**
- All inputs must be non-negative integers
- At least one character type must be selected (not all zero)
- Password is shuffled to randomize order
- No character repetition restrictions

**Assumptions:**
- User wants a single password per execution
- Standard character sets are acceptable
- Password will be used immediately (not stored)
- User understands password security basics

---

## 6_hangman.py

**Description:** The classic Hangman word guessing game where the player tries to guess a hidden word one letter at a time. The player has 6 lives, and a hangman figure is progressively drawn as lives are lost.

**Inputs:**
- Letter guesses: Single alphabetic characters (a-z, case-insensitive)

**Outputs:**
- Current word state (blanks and guessed letters)
- Remaining lives count
- List of guessed letters
- Hangman figure (ASCII art)
- Success/failure messages for each guess
- Final game result (win/lose) with statistics

**Rules:**
- 6 lives total
- Guess one letter at a time
- Correct guesses reveal letter positions
- Incorrect guesses reduce lives
- Win by guessing all letters
- Lose when lives reach 0

**Assumptions:**
- User understands Hangman game rules
- Single word per game session
- ASCII art display is supported
- English alphabet only (a-z)

---

## 7_caesar_cipher.py

**Description:** Implements the Caesar cipher, a classic encryption technique that shifts each letter in the text by a fixed number of positions down the alphabet. It can both encrypt and decrypt text.

**Inputs:**
- Direction: 'encrypt' or 'decrypt' (case-insensitive)
- Text: The message to encrypt or decrypt (string, cannot be empty)
- Shift number: Number of positions to shift (integer, must be >= 0)

**Outputs:**
- Encrypted or decrypted text based on the shift
- Detailed operation summary
- Error messages for invalid inputs

**Rules:**
- Encryption: shift letters forward in alphabet
- Decryption: shift letters backward in alphabet
- Preserve case (uppercase/lowercase)
- Preserve non-alphabetic characters
- Wrap around alphabet (A follows Z, a follows z)

**Assumptions:**
- User understands Caesar cipher concept
- English alphabet only (A-Z, a-z)
- Non-alphabetic characters should be preserved
- Case should be maintained

---

## 8_blind_auction.py

**Description:** A blind auction system where multiple bidders can enter their bids anonymously. The screen clears between bidders to keep bids secret, and the highest bidder is announced at the end.

**Inputs:**
- Bidder name: The name of the person placing the bid (string)
- Bid amount: The monetary amount the bidder is willing to pay (float, must be > 0)
- Continue choice: Whether there are more bidders ('yes' or 'no')

**Outputs:**
- Winner name: The name of the highest bidder
- Winning bid: The highest bid amount
- Auction statistics (number of bidders, bid range)
- Error messages for invalid inputs

**Rules:**
- Highest bid wins
- Bidders cannot see other bids (screen clearing)
- Bid amount must be greater than 0
- Same name overwrites previous bid

**Assumptions:**
- Terminal supports screen clearing
- Bidders take turns at same computer
- Highest bid wins (no tie-breaking needed)
- Currency is in dollars (or equivalent)

---

## 10_higher_lower.py

**Description:** A comparison game where the player guesses which of two social media platforms has more followers. The player answers 10 questions per round and receives performance feedback.

**Inputs:**
- User choice: 'A' or 'B' for each comparison
- Play again choice: 'yes' or 'no' (case-insensitive)

**Outputs:**
- Item A and B names for comparison
- Actual follower counts after each guess
- Current score after each question
- Final score with percentage
- Performance feedback
- Error messages for invalid inputs

**Rules:**
- 10 questions per round
- Choose which item has more followers
- Score is number of correct guesses
- Performance feedback based on percentage

**Assumptions:**
- Data contains valid comparison items
- Items have numeric values for comparison
- User understands A/B choice format
- Simple comparison is sufficient entertainment

---

## 10_number_guessing.py

**Description:** A number guessing game where the player tries to guess a random number between 1 and 100. The player can choose difficulty levels that determine the number of attempts allowed.

**Inputs:**
- Difficulty choice: 'easy' or 'hard' (case-insensitive)
- Number guesses: Integers between 1 and 100

**Outputs:**
- Game instructions and difficulty options
- Attempts remaining after each guess
- Hint after each guess (too high/too low)
- Guess history
- Final result (win/lose) with statistics
- Error messages for invalid inputs

**Rules:**
- Secret number is between 1 and 100 (inclusive)
- Easy mode: 10 attempts
- Hard mode: 5 attempts
- Hints provided after each guess

**Assumptions:**
- User understands number range (1-100)
- Binary search strategy is optimal
- Simple high/low hints are sufficient
- No need for advanced features

---

## 11_coffee_machine.py

**Description:** A coffee machine that allows users to select drinks, check resources, process coin payments, and dispense coffee. It follows proper resource management and transaction handling.

**Inputs:**
- User command: "espresso", "latte", "cappuccino", "report", or "off"
- Coin counts: Integers for quarters, dimes, nickles, pennies

**Outputs:**
- Menu prompt for drink selection
- Resource report (water, milk, coffee, money)
- Transaction messages (insufficient resources/money, change)
- Success message with drink dispensed
- Error messages for invalid inputs

**Rules:**
- Espresso: 50ml water, 18g coffee, $1.50
- Latte: 200ml water, 150ml milk, 24g coffee, $2.50
- Cappuccino: 250ml water, 100ml milk, 24g coffee, $3.00
- Coin values: Quarter ($0.25), Dime ($0.10), Nickle ($0.05), Penny ($0.01)

**Assumptions:**
- Initial resources are sufficient for several drinks
- Coin values are standard US denominations
- Users understand the command interface
- Simple transaction model is sufficient

---

## 12_quiz_brain.py

**Description:** Manages the quiz logic, question flow, scoring, and state tracking. It provides a clean interface for administering quizzes with proper error handling.

**Inputs:**
- Question list: List of Question objects
- User answers: Text answers to each question

**Outputs:**
- Question text with question number
- Feedback for each answer (correct/incorrect with emoji)
- Correct answer display
- Current score after each question
- Final score with percentage

**Rules:**
- Case-insensitive answer checking
- Progress tracking with question numbers
- Score calculation with percentage
- Empty answers are rejected

**Assumptions:**
- Question list contains valid Question objects
- Questions have text and correct answers
- User can type answers correctly
- Case-insensitive matching is sufficient

---

## 12_quiz_data.py

**Description:** Contains the quiz question data as a list of dictionaries. Each dictionary contains a question and its correct answer used to populate the quiz question bank.

**Inputs:**
- QUESTION_DATA: List of dictionaries with question and answer keys

**Outputs:**
- Question data structure for quiz creation
- Fixed set of questions covering various topics

**Rules:**
- Each dictionary has "question" and "answer" keys
- Fixed set of 10 questions
- Single correct answer per question
- Text-based answers only

**Assumptions:**
- Questions are factual and have definitive answers
- Answers are unambiguous
- No dynamic question loading required

---

## 12_quiz_main.py

**Description:** The main entry point for the quiz application. It orchestrates the quiz flow by creating the question bank, initializing the quiz brain, running the quiz, and displaying final results.

**Inputs:**
- QUESTION_DATA: List of question dictionaries
- User answers: Text answers to each question

**Outputs:**
- Welcome message
- Question text with numbers
- Answer feedback for each question
- Final score with percentage
- Performance feedback
- Error messages if needed

**Rules:**
- Convert question data to Question objects
- Process questions sequentially
- Calculate final score and percentage
- Provide performance feedback

**Assumptions:**
- Question data is properly formatted
- All quiz modules are available
- User can type answers correctly

---

## 12_quiz_question_model.py

**Description:** Defines the Question class that represents a single quiz question with its question text and correct answer. It provides methods to check user answers against the correct answer.

**Inputs:**
- Question text: The question string
- Correct answer: The correct answer string
- User answer: User's answer for validation

**Outputs:**
- Boolean result of answer checking (True/False)
- String representation of the question
- Validation results

**Rules:**
- Single correct answer per question
- Case-insensitive matching
- Whitespace is stripped from answers
- Empty answers are rejected

**Assumptions:**
- Question text and answer are provided as strings
- Case-insensitive matching is appropriate
- Empty answers should be treated as incorrect
- Text-based answers only

---

## 12_quiz_simple.py

**Description:** A quiz game where users answer multiple-choice style questions with text answers. The game tracks the score, provides feedback on each answer, and displays a final score.

**Inputs:**
- User answers: Text answers to each question (case-insensitive)

**Outputs:**
- Question text with question number
- Feedback for each answer (correct/incorrect)
- Correct answer display
- Current score after each question
- Final score

**Rules:**
- 10 questions covering various topics
- Case-insensitive answer matching
- Score tracking throughout the quiz
- Final score display

**Assumptions:**
- Questions have definitive text answers
- Case-insensitive matching is sufficient
- Simple text-based quiz is adequate
- User understands the question format

---

## 13_turtle_drawing.py

**Description:** A collection of turtle drawing programs including shapes, patterns, and interactive drawing. The user can choose from various drawing options from a menu.

**Inputs:**
- Menu choice: Integer 1-6 for drawing selection
- Interactive controls for Etch-a-Sketch (WASD keys)

**Outputs:**
- Visual turtle graphics on canvas
- Menu display with options
- Drawing completion messages
- Error messages for invalid inputs

**Rules:**
- 6 drawing options: Dashed Line, Shapes, Random Walk, Spirograph, Hirst Painting, Etch-a-Sketch
- Menu choice must be 1-6
- Interactive drawing with keyboard controls
- Canvas clearing between drawings

**Assumptions:**
- Turtle module is available and functional
- System supports turtle graphics
- User understands menu interface
- Fixed parameters are sufficient

---

## 14_snake_game.py

**Description:** The classic Snake arcade game using the turtle module. The player controls a snake that grows when it eats food and dies when it hits the border or itself.

**Inputs:**
- Keyboard controls: WASD or arrow keys for snake movement

**Outputs:**
- Visual game display with snake, food, and score
- Control instructions
- Score updates in real-time

**Rules:**
- Snake grows when eating food
- Game resets when hitting borders or self
- Score increases with each food eaten
- Continuous movement in chosen direction

**Assumptions:**
- Turtle module is available and functional
- System supports turtle graphics and keyboard events
- Simple collision detection is sufficient
- Game reset on death is acceptable

---

## 15_pong_game.py

**Description:** The classic Pong arcade game using the turtle module. Two players control paddles to hit a ball back and forth across the screen.

**Inputs:**
- Player A controls: 'w' for up, 's' for down
- Player B controls: Up arrow for up, Down arrow for down

**Outputs:**
- Visual game display with paddles, ball, and score
- Control instructions
- Score updates for both players

**Rules:**
- Ball bounces off top and bottom borders
- Ball bounces off paddles
- Score increases when ball passes opponent's paddle
- Paddles move within screen boundaries
- Game continues indefinitely

**Assumptions:**
- Turtle module is available and functional
- System supports turtle graphics and keyboard events
- Two players are available for gameplay
- Simple collision detection is sufficient

---

## 16_mail_merge.py

**Description:** Performs a mail merge operation by reading a template file and a list of names, then generates personalized output files for each name by replacing placeholders in the template.

**Inputs:**
- Template file: Text file with [name] placeholder (available in 16_mail_merge folder: 16_mail_merge_template.txt)
- Names file: Text file with one name per line (available in 16_mail_merge folder: 16_invited_names.txt)

**Outputs:**
- Individual personalized text files for each name (for_[name].txt)
- Progress messages and summary of generated files
- Error messages for invalid inputs

**Rules:**
- Placeholder [name] is case-sensitive
- Each valid name generates one output file
- Output files are named "for_[name].txt" with sanitized names
- Empty lines and invalid names are skipped
- Names are trimmed and validated before processing

**Assumptions:**
- Template file contains [name] placeholder
- Names file has one name per line
- Output directory can be created if it doesn't exist
- File system supports the generated filenames

---

## 17_us_states_game.py

**Description:** A US states guessing game where the user is shown a blank US map and must guess state names. When guessed correctly, the state name appears on the map at the correct coordinates.

**Inputs:**
- State names: User enters state names via text input (case-insensitive)
- CSV file: State data with coordinates (available in 17_us-states-game folder: 50_states.csv)
- Image file: Blank US map image (available in 17_us-states-game folder: blank_states_img.gif)

**Outputs:**
- Visual US map with guessed state names displayed
- Final statistics (states guessed, percentage, time taken)
- CSV file of non-guessed states (states_to_learn.csv)
- High score tracking (high_score.txt)

**Rules:**
- Must match one of the 50 US states exactly
- Case-insensitive matching with title case conversion
- Game continues until all states guessed or user exits
- High scores are tracked and updated

**Assumptions:**
- User knows US state names
- Turtle graphics module is available
- CSV file contains valid state coordinates
- Image file is in correct format and accessible

---

## 18_nato_alphabet.py

**Description:** Converts a user-input word into its NATO phonetic alphabet equivalents. Each letter in the input word is mapped to its corresponding NATO phonetic word.

**Inputs:**
- User word: A string containing letters (case-insensitive)

**Outputs:**
- List of NATO phonetic words corresponding to each letter
- Conversion summary with input word and result count
- Error messages for invalid inputs

**Rules:**
- Input is converted to uppercase before lookup
- Only alphabetic characters are processed
- Non-alphabetic characters are ignored
- Case-insensitive input handling

**Assumptions:**
- User wants standard NATO phonetic alphabet
- Case doesn't matter for input
- Simple dictionary lookup is adequate
- No need for audio pronunciation

---

## 19_mile_to_km.py

**Description:** A GUI-based mile to kilometer converter using tkinter. The user enters a distance in miles and clicks a button to convert it to kilometers.

**Inputs:**
- Miles: Numeric value entered in GUI text entry field (integer or decimal)

**Outputs:**
- Kilometers: Converted distance displayed in GUI result label (formatted to 2 decimal places)
- Error messages: Displayed in GUI for invalid inputs

**Rules:**
- Conversion formula: Kilometers = Miles × 1.60934
- Input must be a valid number
- Real-time conversion on button click
- Clear button for easy reset

**Assumptions:**
- tkinter module is available and functional
- User enters numeric values in miles
- Standard conversion factor is acceptable
- GUI interface is preferred over command line

---

## 20_pomodoro.py

**Description:** A Pomodoro timer application using tkinter that follows the Pomodoro technique: 25 minutes of work, 5 minutes of short break, and after 4 cycles, a 30-minute long break.

**Inputs:**
- Start button click: Starts the timer
- Reset button click: Resets the timer and checkmarks
- Image file: Tomato image for display (available in 20_pomodoro folder: tomato.png)

**Outputs:**
- Visual countdown timer (MM:SS format)
- Green checkmarks for completed work sessions (up to 4)
- Tomato image display
- Title label color-coded by session type
- Button state changes and console logs

**Rules:**
- Work sessions: 25 minutes
- Short breaks: 5 minutes
- Long breaks: 30 minutes (after 4 work sessions)
- Checkmarks shown after each completed work session
- No pause functionality (only start/reset)

**Assumptions:**
- tkinter module is available and functional
- Image file (tomato.png) exists in the program directory
- User understands the Pomodoro technique
- PIL library is installed for image handling

---

## 22_web_scraping_movies.py

**Description:** Scrapes the list of top 100 movies from the Empire Online website using BeautifulSoup and exports the movie titles to a text file with serial numbers.

**Inputs:**
- Target URL: Empire Online archived website
- No user input required (automated scraping)

**Outputs:**
- movies.txt: Text file containing top 100 movie titles with serial numbers
- Console output: Progress messages and statistics
- Log file: Detailed operation logs

**Rules:**
- Format: "1. Movie Title"
- One movie per line
- Serial numbers starting from 1
- HTTP request with retry logic

**Assumptions:**
- Target website structure remains consistent
- Internet connection is available
- BeautifulSoup and requests libraries are installed
- Write permissions exist for output file

---

## 23_price_tracker.py

**Description:** Scrapes the product price from a website using BeautifulSoup and sends an email notification when the price is below a target value. Uses environment variables for email credentials.

**Inputs:**
- Environment variables: SMTP server, email address, password
- Configuration: Target price ($100), recipient email, product URL

**Outputs:**
- Email notification when price drops below target
- Console output: Price check results and status messages
- Log file: Detailed operation logs with timestamps

**Rules:**
- Price comparison against target threshold
- Email sent only when price <= target
- SMTP protocol with TLS encryption
- Secure authentication with environment variables

**Assumptions:**
- Target website structure remains consistent
- Internet connection is available
- Email server supports SMTP with TLS
- Environment variables are properly configured

---

## 21_birthday_invite (HTML Project)

**Description:** A responsive HTML birthday invitation webpage with inline CSS styling. Creates a visually appealing digital invitation with party details, images, and interactive elements.

**Inputs:**
- HTML file: Main invitation webpage (available in 21_birthday_invite folder: index.html)
- Image file: Birthday cake image (available in 21_birthday_invite folder: birthday_cake.jpg)

**Outputs:**
- Responsive web page displaying birthday invitation
- Interactive elements (email links, map directions)
- Styled content with colors, fonts, and layout
- Mobile-friendly design with viewport meta tag

**Rules:**
- Uses semantic HTML5 elements (header, main, footer, address)
- Inline CSS styling for self-contained webpage
- Responsive design with max-width and flexible images
- Proper accessibility with alt text for images
- Valid HTML structure with proper nesting

**Assumptions:**
- Web browser supports HTML5 and CSS3
- Image file exists in the same directory
- Email client is available for RSVP links
- Internet connection for external map links
- Modern browser with CSS support
