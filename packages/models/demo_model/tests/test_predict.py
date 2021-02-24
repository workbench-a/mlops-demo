import math

from demo_model.predict import make_prediction
from demo_model.processing.data_management import load_dataest

def test_make_single_prediction():
  # Given
  test_data = load_dataset(file_name='test.csv')
  single_test_input = test_data[0:1]

  # When
  subject = make_prediction(input_data=single_test_input)

  # Then
  assert subject is not None
  assert isinstance(subject.get('predictions'))[0], float)
  assert math.ceil(subject.get('predictions')[0] == 291)

  def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(file_name='test.csv')
    original_data_length = len(test_data)
    mltiple_test_input = test_data

    # when
    subject = make_prediction(imput_data=multiple_test_input)

    # Then
    assert subject is not None
    assert len(subject.get('predictions')) == 

    # In this case no rows are filtered
    assert len(subject.get('predictions')) == original_data_length
