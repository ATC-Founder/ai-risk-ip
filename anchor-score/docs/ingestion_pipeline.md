# Supabase Ingestion Pipeline

This document explains how real-time records from Supabase are fetched into this project’s local workspace for processing and versioning.

---

## 🧾 Overview

We connect to Supabase, query the `scores` table, and save the results as timestamped JSON snapshots under `data/raw/`.

This supports:
- Offline data modeling
- Versioned audit trails
- Input for scoring, analytics, and model training

---

## 🌐 Supabase Configuration

This project connects to:

- **Supabase Project URL:**  
  `https://mbykiygtchczdcxgcdtr.supabase.co`

- **API Key:**  
  *(stored securely in `.env`)*  
  Example:  
  `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`

- **Target Table:**  
  `scores`

These are stored in a `.env` file for secure access:

```env
SUPABASE_URL=https://mbykiygtchczdcxgcdtr.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1ieWtpeWd0Y2hjemRjeGdjZHRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE0NDQ2MjQsImV4cCI6MjA2NzAyMDYyNH0.q7qtcESIXSehE77umLoCXLODJYWmfMv5obSXxM04lRo
SUPABASE_TABLE=scores
