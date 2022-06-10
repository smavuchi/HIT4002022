The following tools should be installed on your machine:
- Python 3.7.3 (On Python installation make sure the "Add to path variables" checkbox is ticked.) 
- NodeJs (To be used for the ReactJs Frontend plus Solidity backend)
- Truffle Framework (Offers a set of tools for developing Ethereum smart contracts)
- Ganache (Personal Blockchain)
- Metamask Ethereum Wallet (Google Chrome Extension that will allow us to connect our Chrome browser to the blockchain network.)
- Git
- VS Code

Installing frontend dependencies:
- Click on the file named frontend_install_dependencies in this project's root folder, a terminal window should open up and the installation procedures should start automatically.
- This installation process will only work if you have a working internet connection and if you have NodeJs installed.

Installing Python backend dependencies:
- First visit https://github.com/ageitgey/face_recognition#installing-on-windows and follow the installation instructions. It's important that you do this before moving to the next step.
- Click on the file named python_backend_install_dependencies in this project's root folder, a terminal window should open up and the installation procedures should start automatically.
- This installation process will only work if you have a working internet connection and if you have Python 3.7.3 installed.

Starting the Blockchain backend:
- Open Ganache
- Click on the file named truffle_compile , ignore the experimental feature warnings, wanted to check if they now support extracting arrays.
- If it's the first time you're running the Dapp on your machine, click on the file named truffle_migrate
- If there's been an update made, click on the file named truffle_migrate_reset

Staring the Python backend server:
- Click on the file named start_python_backend in this project's root folder, a terminal window should pop up.
- This will only work if the Python backend's dependencies were installed successfully.

Starting the frontend server:
- Click on the file named start_frontend in this project's root folder, a terminal window should pop up. When the the server is up and running you should be redirected to your browser using the address that the project is running on. If for some reason the server starts but you are not redirected after its fully up and running, open your browser and visit localhost:3000 / localhost:3001 if your port 3000 is taken by some other process.
- This will only work if the frontend's dependencies were installed successfully, and if you have Ganache installed and running, plus Meta Mask installed and configured properly.

Setting up Meta Mask:
- Visit https://medium.com/@kacharlabhargav21/using-ganache-with-remix-and-metamask-446fe5748ccf 
- Scroll down to the title "Using Ganache with Metamask" , follow the steps listed there, use the images for a visual assist. The Ganache RPC Http URL needed is printed under the label "RPC server" in Ganache, its normally http://127.0.0.1:7545. In the case that its different from the one I listed, open truffle-config.js, head over to line 48 and change the written port to the one listed in your Ganache. Only follow the instructions up until the line "Any transactions you make with this account in Metamask, the same balance will be reflected in Ganache and vice-versa", the rest doesn't apply in this setup.
- Make sure the ports in your truffle-config, Meta Mask and Ganache are exactly the same.

Downloading updates:
- To download any updates made, click of the update file.
- If any changes were made on your side, a git stash is required before updating otherwise you'll get an error, click on the git_stash_changes file