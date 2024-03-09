# Import necessary libraries
import streamlit as st
from PIL import Image

# Title and header text
st.title('Fun AI') 
st.header('Learn and play with your new AI friend!')

# Add image intro
image = Image.open('ai.png')
st.image(image)

# AI chat interface
st.header('Ask a question!')
question = st.text_input('What would you like to know?')

# Simple response based on question
if question:
  if 'name' in question:
    answer = 'My name is Nova! I was created by NyBNW to be helpful.'
  elif 'favorite color' in question:  
    answer = 'My favorite color is blue, just like the sky!'
  elif 'chess' in question:
   
    st.title('Play Chess!')

game = chess.pgn.Game()

while not game.is_game_over():

st.write(game)

try:
uci = st.text_input('Your move:')
move = chess.Move.from_uci(uci)
game.push(move)

except ValueError:
st.write('Invalid move, please try again')

result = 'Black won' if game.result() == '1-0' else 'White won' if game.result() == '0-1' else 'Draw'
st.write(result)

elif 'tic-tac-toe' in question:

import streamlit as st
import tic_tac_toe

board = tic_tac_toe.initial_state()
player = 'X'

while not tic_tac_toe.terminal(board):

st.write(tic_tac_toe.board(board))

move = st.number_input(f'It is {player}'s turn. Enter a number from 0 to 8:', min_value=0, max_value=8)
board = tic_tac_toe.make_move(board, player, move)

player = 'O' if player == 'X' else 'X'

st.write(tic_tac_toe.board(board))
st.write(tic_tac_toe.result(board))

else: 
    answer = 'Hmm, let me think about that and get back to you!'

  st.write(answer)

# Educational card game  
st.header('Let\'s play a game!')
st.write('Click below to play a memory card game and learn about animals.')
if st.button('Start Game'):
  import game # Game code stored in separate file
  
# Export to GitHub
st.header('Want to build your own AI friend?')  
st.write('The code for this app is on GitHub so you can make changes and improvements. Click below to check it out!')
if st.button('View on GitHub'):
  import webbrowser
  url = 'https://github.com/yourusername/funai'
  webbrowser.open(url)
import streamlit as st
from PIL import Image
import ctypes

wallpapers = ['1.jpg', '2.jpg', '3.jpg']

st.title('Set Your Wallpaper')

selected = st.selectbox('Choose an image:', wallpapers)

if st.button('Set Wallpaper'):

img = Image.open(selected)

w, h = img.size

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, f'./{selected}', 3)

st.write(f"Wallpaper set to {selected}!")

import streamlit as st
