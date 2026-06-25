class TelemetryEvaluator:
    def __init__(self, system_tag, points):
        self.system_tag = system_tag
        self.points = points

    def count_boundary_breaches(self, ceiling_mark):
        breach_count = 0
        for entry in self.points:
            if entry > ceiling_mark:
                breach_count = breach_count + 1
        return breach_count

    def analyze_consecutive_drops(self):
        for i in range(len(self.points) - 1):
            step_drop = self.points[i] - self.points[i+1]
            if step_drop > 40:
                return "Critical Drop Detected"
        return "Signal Steady"

pressure_logs =
analyzer = TelemetryEvaluator("SYS-CORE-5", pressure_logs)

print(analyzer.count_boundary_breaches(110))
print(analyzer.analyze_consecutive_drops())
