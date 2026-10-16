from dataclasses import dataclass

@dataclass
class Change:
    feature: str
    impact: int
    likelihood: int
    change_size: int

def score(change: Change) -> int:
    return change.impact * change.likelihood + change.change_size

if __name__ == '__main__':
    checkout = Change('Checkout', impact=5, likelihood=4, change_size=3)
    print({'feature': checkout.feature, 'risk_score': score(checkout), 'priority': 'P0'})
