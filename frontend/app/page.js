import styles from "./page.module.css";

export default function Home() {

  const games = [
    {
    id: 1,
    awayTeam: "Yankees",
    awayScore: 4,
    homeTeam: "Red Sox",
    homeScore: 5,
    status: "Live",
    },
    {
      id: 2,
      awayTeam: "Giants",
      awayScore: "-",
      homeTeam: "Dodgers",
      homeScore: "-",
      status: "12:00 PM EST",
    },
  ]

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        
        <header className={styles.header}>
          <h1>Baseball Dashboard</h1>
          <p>Live Games</p>
        </header>
        
        
        <section className={styles.gamesSection}>
          {games.length === 0 ? (
            <p>No games today.</p>
          ):(
            games.map((game, index) => (
              <div key={index} className={styles.gameCard}>
                <div className={styles.teamRow}>
                  <span>{game.awayTeam}</span>
                  <span>{game.awayScore}</span>
                </div>
                <div className={styles.teamRow}>
                  <span>{game.homeTeam}</span>
                  <span>{game.homeScore}</span>
                </div>
                <p className={styles.gameStatus}>{game.status}</p>
              </div>
            ))
          )}
        </section>
      </main>
    </div>
  );
}
