from app.models import Employee, Engineer, Manager


def insert_employees(db):
    if not db.session.query(Employee).first():
        # Create employees
        employees = []
        for i in range(5):
            employees.append(
                Engineer(
                    name=f"Engineer {i + 1}",
                    type="engineer",
                    engineer_info=f"Info {i + 1}",
                )
            )
            employees.append(
                Manager(
                    name=f"Manager {i + 1}",
                    type="manager",
                    manager_data=f"Data {i + 1}",
                )
            )

        # Add and commit to the session
        db.session.bulk_save_objects(employees)
        db.session.commit()
