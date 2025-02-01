from datetime import date
from sqlalchemy import select, update, func

class EndOfMonthLogic:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def check_and_update_current_month(self):
        current_month_start = date.today().replace(day=1)
        with self.db_handler.session_scope() as session:
            # Query the persistent_state table for the current_month state_key
            result = session.execute(
                select(self.db_handler.persistent_state.c.last_updated)
                .where(self.db_handler.persistent_state.c.state_key == 'current_month')
            ).fetchone()

            if result:
                last_updated = result[0]
                # Convert last_updated to date for comparison
                if last_updated and last_updated.date() >= current_month_start:
                    print("Debug: Current month is up to date")
                else:
                    print("Debug: Invoking end of month processing")
                    # Update the last_updated field
                    session.execute(
                        update(self.db_handler.persistent_state)
                        .where(self.db_handler.persistent_state.c.state_key == 'current_month')
                        .values(last_updated=func.now())
                    )
            else:
                print("Debug: Invoking end of month processing")
                # Update the last_updated field for the current_month state_key
                session.execute(
                    update(self.db_handler.persistent_state)
                    .where(self.db_handler.persistent_state.c.state_key == 'current_month')
                    .values(last_updated=func.now())
                )