# Dev Log - PokePort    
> A session-based developer log capturing progress, learning, blockers, and insights throughout the build of PokePort: a Pokémon Card Investment Tracker + Grading Estimator.

## 🗓️ [Session Date: DD-MM-YYYY]  
### ⏱ Duration: 

### ✅ What I Worked On

### 💡 Why I Worked on This

### 🔍 What I Learned / Practiced

### 🤯 What Was Challenging

### 🧠 Key Insight or “Aha!” Moment

### 🔄 Next Step / Todo for Next Session

### 🔗 Git Commit(s)

---

## 🗓️ [Session Date: 12-06-2025]  
### ⏱ Duration: 1 x 1.5 Hours 1 x 3 Hours

### ✅ What I Worked On
- SQL Basics
- Using SQLite in Python
- Troubleshooting import errors

### 💡 Why I Worked on This
As this current project relies on using data stored within a database for our card collection, an understanding of how to create, use and manipulate a database is necessary. I needed to setup how card information would be stored and couldn't do that until I first knew the "how to" of SQLite.

### 🔍 What I Learned / Practiced
- Basic SQL syntax (database creation, table creation, adding and manipulating data)
- How to use SQLite in Python (connecting to a database, initializing a cursor for command execution, creating a table)
- Using `sqlite3.connect()` inside a context manager, ensuring database connection is closed properly
- How to import function across directories within a project successfully 
- That `__init__.py` needs to be within the directory you want to import from , if importing from another directory 

### 🤯 What Was Challenging
Remembering SQL syntax was a struggle, however this is expected as I have no prior experience with SQL and the initial learning curve is expected to be a little steep. By the time I developed the function to initialize the data base using sqlite some of the syntax started to sink into my memory allowing me to write the code faster. As I use SQL and SQLite more often the syntax will come to me more promptly. 

The troubleshooting of importing across directories proved to be challenging, causing me around an hour of trying to debug what what going wrong with testing the `init_db()` in `cli.py`. After reviewing several solutions and tinkering with the line of import code I managed to resolve the issue and strengthen my understanding of why is wasn't working and what to do in the future - ultimately where I was trying to run the code within the project directory was the fault and using `python -m interface.cli` in the root of the directory is what saved me and allowed the database file to initialize.  

### 🧠 Key Insight or “Aha!” Moment
- Understanding that the cursor acts a 'translator' of sorts, executing SQL commands
- When I understood why I couldn't run `cli.py` and that I needed to be within the root of the directory within the terminal to run `python -m interface.cli` and get the `init_db()` function to work 

### 🔄 Next Step / Todo for Next Session
- Begin build of first storage function `add_card()`

### 🔗 Git Commit(s)

---

## 🗓️ [Session Date: 11-06-2025]  
### ⏱ Duration: 2 Hours 

### ✅ What I Worked On
- Developing the user stories and edge cases for the PokePort project
- Decided on a storage format for the PokePort database 
- Designed the initial database schema 

### 💡 Why I Worked on This
- Clear user stories will let me know what to define as core functionality 
- By deciding on a storage format for the PokePort data, I can proceed with developing core functions to
  obtain that data. This also open a leaning stream for me to further enhance my knowledge in SQLite. 

### 🔍 What I Learned / Practiced
- I learned the importance of clear, thought out user stories and how the are used to decide core functionality.
- I've also began learning the basics of database design and SQLite.  

### 🤯 What Was Challenging
I found it challenging to trust in what I had wrote in my documentation and designs as being "correct" or "suitable". As I am not in industry, the documentation I am writing is a first, leaving me "is this correct?" or "should it look like this?". 

### 🧠 Key Insight or “Aha!” Moment
- The importance of user stories to help break down core functionality, ensuring focus on core MVP development.

### 🔄 Next Step / Todo for Next Session
- Research SQLite basics within Python
- Create `storage.py` file
- Write code that: Connect to SQLite file, creates the table, uses the schema design

### 🔗 Git Commit(s)

---

## Week 1 Recap - Project Setup & Planning 
### Duration: Approx. 5-10 hours (spread across multiple sessions)

### ✅ What I Worked On
- Set up GitHub repository for PokePort
- Connected local repo to remote and pushed initial commit
- Created GitHub Project Board (Backlog, To Do, In Progress, Done)
- Created GitHub Issues for all Phase 1 tasks
- Wrote `project_scope.md` — defined the problem, user, MVP, and stretch goals
- Drafted `features_mvp.md` — listed core and optional features
- Sketched out timeline for an 8–12 week build

### Why I Worked On This
> Phase 1 of the PokePort project is all about defining the what, why, and how - setting a foundation for the whole project.

### What I Learned / Practiced  
- How to translate loose ideas into a scoped MVP
- Importance of timeline chunking to reduce overload
- Using GitHub Issues and Projects like real dev workflows 
- How to balance clarity and detail in Git commit messages.
- What features_mvp and project_scope documentation looks like
- How to effectively use Git branching to separate new features, documentation, and updates for cleaner version control.

### What Was Challenging
- Avoiding over-complicating / over-thinking documentation detail within `project_scope.md` and `features_mvp.md`
- Deciding what to defer to stretch goals to keep MVP realistic
- Getting comfortable with documenting even the planning phase

### Key Insight or "Aha!" Moment 
> Planning **is** an important part of development and although it can take longer than initially thought - it saves you from future burnout and messy rewrites

### Next Step / Todo for Next Session
- Write 5 user stories and priorities them in the dev log or as GitHub Issues
- Draft the basic card schema (e.g. name, set, condition, price, date)
- Decide on storage format: JSON for now or go straight to SQLite?

### 🔗 Git Commit(s)
> `git commit -m "Add initial dev_log entry summarizing Week 1 planning and setup"`
