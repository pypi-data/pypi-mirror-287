import logging

from asrch.modules.logging_formatter import ColorFormatter

c_log = logging.getLogger(__name__)
c_log.setLevel(logging.DEBUG)

sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")

sh.setFormatter(c_form)

c_log.addHandler(sh)


def test_logs(caplog):
    c_log.debug("d_message")
    c_log.info("i_message")
    c_log.warning("w_message")
    c_log.error("e_message")
    c_log.critical("c_message")

    assert "test_logger_test.py" and "DEBUG" and "d_message" and "19" in caplog.text
    assert "test_logger_test.py" and "INFO" and "i_message" and "19" in caplog.text
    assert "test_logger_test.py" and "WARNING" and "w_message" and "19" in caplog.text
    assert "test_logger_test.py" and "ERROR" and "e_message" and "19" in caplog.text
    assert "test_logger_test.py" and "CRITICAL" and "c_message" and "19" in caplog.text

    caplog.clear()
