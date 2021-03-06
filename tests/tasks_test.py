from pytest import fail

from nekoyume.tasks import block_broadcast


def test_muted_attribute_error(fx_session):
    try:
        block_broadcast(0,
                        'http://localhost:5000',
                        'http://localhsot:5001',
                        session=fx_session)
    except AttributeError:
        fail('broadcast tasks should not raise AttributeError.')
