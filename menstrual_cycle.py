from datetime import datetime, timedelta

print("Name:")
name = input()

print("Enter your Cycle length:")
cycleLength = int(input())

print("Generate flow report for how many month:")
months = int(input())

print("Date of last flow (in the format of DD/MM/YYYY):")
inputDate = input()
lastFlowDate = datetime.strptime(inputDate, '%d/%m/%Y')

print("Do you want to see your Flow Report (Yes/No)?:")
showReport = input()

if showReport.lower() == "yes":
    print("Please wait while we generate your flow report......")
    print()
    print("Loading >>>>>>>>>>>>>>>>>>>>>>")
    print()
    print("=====================================")
    print("Flow report is loaded successfully!!!")
    print("=====================================")
    print()
    print("             FLOW REPORT                  ")
    print("==========================================")
    print()

    nextFlowDate = lastFlowDate + timedelta(days=cycleLength)
    print("Next Flow Date:", nextFlowDate.strftime('%d/%m/%Y'))

    ovulationDate = lastFlowDate + timedelta(days=cycleLength - 14)
    print("Ovulation Date:", ovulationDate.strftime('%d/%m/%Y'))

    fertileStart = ovulationDate - timedelta(days=3)
    fertileEnd = ovulationDate + timedelta(days=4)
    print("Fertile Period:", fertileStart.strftime('%d/%m/%Y'), "to", fertileEnd.strftime('%d/%m/%Y'))

    freePeriodStart1 = lastFlowDate + timedelta(days=4)
    freePeriodEnd1 = lastFlowDate + timedelta(days=9)
    freePeriodStart2 = nextFlowDate - timedelta(days=9)
    freePeriodEnd2 = nextFlowDate - timedelta(days=4)
    print("Safe Period:", freePeriodStart1.strftime('%d/%m/%Y'), "to", freePeriodEnd1.strftime('%d/%m/%Y'), "and",
          freePeriodStart2.strftime('%d/%m/%Y'), "to", freePeriodEnd2.strftime('%d/%m/%Y'))

    nextFlowPeriodStart = nextFlowDate - timedelta(days=3)
    nextFlowPeriodEnd = nextFlowDate + timedelta(days=3)
    print("Next Flow Period:", nextFlowPeriodStart.strftime('%d/%m/%Y'), "to", nextFlowPeriodEnd.strftime('%d/%m/%Y'))
    print("==========================================")
