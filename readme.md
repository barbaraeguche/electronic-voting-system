# electronic voting system 🗳️
a minimal voting system that offers candidate listings, user voting capabilities, real-time result displays, and the option to add new candidates seamlessly.

## features 👾
- **candidate display:**  displays a list of eligible candidates for voting.
- **voting process:** allows users to cast their votes, maintaining integrity.
- **add candidates:** enables the addition of new candidates to the existing list.
- **results overview:** displays a comprehensive list of electoral results, accounting for ties.
- **terminate system:** gracefully exits the voting system with a closing message.

## limitations 🚨
- **candidate ids**: the system currently lacks validation to ensure the uniqueness of candidate ids, which may lead to potential conflicts in data management.
- **input validation**: the input validation mechanism is limited to recognizing only the format of `id, name` separated by a `;`. it does not accommodate alternative input formats, which could restrict user flexibility.
- **user interface**: the user interface may become cluttered when displaying longer candidate ids and names, impacting overall readability and user experience.

## running the project 🏁
to get the project up and running on your local machine, follow these steps:

- **ensure python is installed:** must have [python version ^3.11](https://www.python.org/downloads/) installed.
- **clone the repository:**
```bash
git clone https://github.com/barbaraeguche/electronic-voting-system.git
```
- **navigate to the project directory:**
```bash
cd electronic-voting-system
```
- **run the project:**
```bash
python3 driver.py
```

## gallery 📸
<details>
  <summary>showcase</summary>

  - **initial run**<br>
  ![init](https://github.com/user-attachments/assets/b68d8559-373f-4c4e-9df3-ca07c97d9975)

  - **option 1**<br>

  
  - **option 2**<br>

  
  - **option 4**<br>

</details>
