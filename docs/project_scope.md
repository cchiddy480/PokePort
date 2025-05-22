# 📌 Project Scope: PokePort

## 🧠 Summary

>PokePort is an independent open-sourced project to act as a tool for Pokemon TCG card collectors to manage and gain insight into the "return of investment" of their collections, whilst also allowing for initial insights into the grading potential of their cards. The goal is to create an open-sourced collection management platform for collectors without the need for subscriptions or payment for access. 


## 👤 Target User

- Pokemon TCG card collectors, looking for a local and inexpensive solution to manage their collection

- Pokemon TCG card investors looking to gain insight in the potential "return on investment" of their card collection

- Individuals with the intention to have their cards professionally graded and wanting to gain insight into the grading potential of their card before hand


## 🔍 The Problem

There are currently several "portfolio" tracking solutions available allowing users to keep track of their card collections as an investment and identify the current worth of those collectors via current value graphs. This allows users to identify if they are currently making a gain or loss but typically require a monthly subscription or initial one off payment to access more advanced features. What these solutions do not typically offer is:

- An insight into the potential ROI of the cards within users collections
- A completely free, non pay-walled, solution providing all the necessary tools a collector of trading cards may need or want
- A system that allows users to gain insight into the grading potential of specific cards based on submitted photos 

The development of PokePort aims to alleviate these problems. 

## 🧱 Core Features (Must-Have)

**Card collection tracking** - Add, update, and remove cards and card details in a collection stored locally via CSV or JSON

**Value tracking** - Obtain current market value via manual input or auto-fetch. Calculate and display: profit/loss per card, total invested value vs total value, ROI%

**Grading estimator (Manual input)** - User inputs via Y/N scales: centering, whitening, scratches, corners (good/bad). Logic tree outputs grading likelihood (e.g "Estimated: PSA 8-9")

**Interface (CLI or Streamlit)** - Simple UI to: view cards, see ROI, estimate grades, navigate collection

## ✨ Nice-to-Have Features (Stretch / Extended Goals)

**Image-Based Grading Assist** - Upload front/back card images, simulate visual grading using basic rules or OpenCV

**Dashboards & Reports** - ROI over time chart (Matplotlib / plotly), value breakdown per set or grade, export collection report as PDF or CSV

**API Intergration** - Live value lookup via: eBay sold listings, TCGPlayer API, compare PSA 9 vs PSA 10 price estimates

**Notifications & Insights** - Alert if a card spikes in value, recommend "sell" or "grade" actions based on ROI thresholds

**User Profiles** - Save/load different collections, add basic login/auth for multiple users (stretch)

**Deployment** - Deploy Streamlit app via Streamlit cloud, share demo & sample dataset

## ⏳ Timeline Overview
| Phase            | Focus                                        | Target Week |
|------------------|----------------------------------------------|-------------|
| Week 1           | Setup repo, define scope, plan MVP           | Week 1      |
| Week 2–3         | Build collection manager + local storage     | Week 2–3    |
| Week 4–5         | Add static/API-based price lookup + ROI calc | Week 4–5    |
| Week 6–7         | Add grading estimator logic                  | Week 6–7    |
| Week 8–9         | Implement Streamlit UI (or polish CLI)       | Week 8–9    |
| Week 10–11       | Testing, cleanup, code reviews               | Week 10–11  |
| Week 12          | Final polish, documentation, showcase ready  | Week 12     |

## 🎯 Learning Goals
- Plan and build a full MVP using modular Python, Git, and real developer workflows
- Work with JSON and SQLite to manage and persist card collection data
- Integrate a pricing API or scraper to calculate ROI from live or static data
- Build a basic Streamlit UI to make the tool usable and presentable
- Create clean commit messages, manage issues, and reflect in dev logs
- Use data visualization to show investment trends and grading performance

