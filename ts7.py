from typing import Any
def validate_coords(*coords: tuple[float, float]) -> list[dict[str, Any]]:
    if type(coords) != tuple:
        raise TypeError('Координаты должны быть кортежем')
    ans = []

    for lat, lng in coords:
        errors = []

        if lat < -90 or lat > 90:
            errors.append(f'Неверно задана широта: {lat} 'f'(должна быть от -90.0 до 90.0)')

        if lng < -180 or lng > 180:
            errors.append(f'Неверно задана долгота: {lng} 'f'(должна быть от -180.0 до 180.0)')

        if errors:
            ans.append({
                'lat': lat,
                'lng': lng,
                'error': '; '.join(errors)
            })

    return ans

print(validate_coords(
(0.0, 1.0),
(-35.7, -100.7),
(-95.0, 120.5),
(88.8, 190.5),
(17.33, 18.46),
(-120.0, -200.1),))