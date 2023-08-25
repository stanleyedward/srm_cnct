# srm_cnct
automation to connect to SRMIST wifi
1. Clone the repo to your directory
    ```sh
    git clone https://github.com/stanleyedward/srm_cnct.git
    ```
2. open your `.bashrc` file or `.zshrc` if you're using zsh
   ```sh
   nano .bashrc
   ```
   ```sh
   nano .zshrc
   ```
3. add `main.py` as an alias
   ```sh
   alias srm_connect="python3 $HOME/srm_cnct/main.py"
   ```
3. Save and exit then,
   ```sh
   source ~/.bashrc 
   ```

   ```sh
   source ~/.zshrc  
   ```
   or restart the terminal

4. Run the alias cmd
    ```sh
    srm_connect
    ```
5. Input user and password for one-time setup (both are stored locally)
   ```sh
   input username:xx1234
   input password:qwerty@2345
   ```
6. Rerun alias after setup, connect to ssid:SRMIST before hand. You should see:
   ```Initializing```
   ```Network Access Granted```
  
