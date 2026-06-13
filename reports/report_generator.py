from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_report():

    pdf = SimpleDocTemplate(
        "outputs/location_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "IoT Vehicle Tracking Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Vehicle tracking data collected successfully.",
            styles["BodyText"]
        )
    )

    pdf.build(content)

if __name__ == "__main__":
    generate_report()