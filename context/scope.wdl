workflow hello {
  # (a) π is calculated in this step.
  call calculate_pi

  # (b) the output from the `calculate_pi` step is passed to
  # the input of the `calculate_circle_area` input here.
  call calculate_circle_area { input: pi = calculate_pi.pi }

  output {
    Float area = calculate_circle_area.area
  }
}