def can_make_calls(flight_mode: bool, signal_strength: int) -> bool:
    """
    Function:
                can_make_calls
    Inputs:
                signal_strength, integer
                flight_mode, boolean
    Pre-conditions:
                0 <= signal_strength <= 4
                flight_mode True when enabled, False when disabled.
    Output:
                boolean True if the phone is able to make and receive calls, False if unable.
    Post-conditions:
                returns True if and only if flight_mode = False AND (signal strength >= 2)
    """
    return (not flight_mode) and signal_strength >= 2


if __name__ == '__main__':
    assert can_make_calls(flight_mode=False, signal_strength=0) is False
    assert can_make_calls(flight_mode=False, signal_strength=1) is False
    assert can_make_calls(flight_mode=False, signal_strength=2) is True
    assert can_make_calls(flight_mode=False, signal_strength=3) is True
    assert can_make_calls(flight_mode=False, signal_strength=4) is True
    assert can_make_calls(flight_mode=True, signal_strength=0) is False
    assert can_make_calls(flight_mode=True, signal_strength=1) is False
    assert can_make_calls(flight_mode=True, signal_strength=2) is False
    assert can_make_calls(flight_mode=True, signal_strength=3) is False
    assert can_make_calls(flight_mode=True, signal_strength=4) is False
