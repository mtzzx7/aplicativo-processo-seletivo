import sqlite3

def get_connection():
    return sqlite3.connect("selection.db")

def get_dashboard_cards():
    conn = get_connection()
    cur = conn.cursor()

    cards = {}
    cards["inscritos"] = cur.execute("SELECT COUNT(*) FROM candidates").fetchone()[0]
    cards["equipes"] = cur.execute("SELECT COUNT(*) FROM teams").fetchone()[0]
    cards["avaliacoes"] = cur.execute("SELECT COUNT(*) FROM evaluations").fetchone()[0]
    cards["status"] = cur.execute("SELECT value FROM settings WHERE key='process_status'").fetchone()[0]

    conn.close()
    return cards

def get_scores():
    # conn = get_connection()
    # cur = conn.cursor()

    # scores = [
    #     row[0] for row in cur.execute(
    #         "SELECT score_final FROM candidates WHERE score_final IS NOT NULL"
    #     )
    # ]

    # conn.close()
    return []


def get_stage_averages():
    conn = get_connection()
    cur = conn.cursor()

    row = cur.execute("""
        SELECT
            AVG(immersion),
            AVG(development),
            AVG(presentation)
        FROM evaluations
        WHERE is_active = 1
    """).fetchone()

    conn.close()
    return row

def get_presence_vs_score():
    # conn = get_connection()
    # cur = conn.cursor()

    # data = cur.execute("""
    #     SELECT presence_percent, score_final
    #     FROM candidates
    #     WHERE score_final IS NOT NULL
    # """).fetchall()

    # conn.close()
    return []


def get_team_averages():
    # conn = get_connection()
    # cur = conn.cursor()

    # data = cur.execute("""
    #     SELECT team_id, AVG(score_final)
    #     FROM candidates
    #     WHERE score_final IS NOT NULL
    #     GROUP BY team_id
    #     ORDER BY team_id
    # """).fetchall()

    # conn.close()
    return []
