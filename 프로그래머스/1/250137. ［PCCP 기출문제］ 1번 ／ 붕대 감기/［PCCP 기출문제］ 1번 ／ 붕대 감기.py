
def solution(bandage, health, attacks):
    t, x, y = bandage  # 시전 시간 t, 초당 회복량 x, 추가 회복량 y
    current_health = health  # 현재 체력
    max_health = health  # 최대 체력
    current_time = 0  # 현재 시간
    consecutive_success = 0  # 연속 성공한 시간
    attack_index = 0  # 공격 인덱스 (현재 처리 중인 공격)
    
    # 전체 시간을 1초씩 시뮬레이션
    for time in range(1, attacks[-1][0] + 1):
        # 현재 시간에 공격이 있는지 확인
        if attack_index < len(attacks) and time == attacks[attack_index][0]:
            # 몬스터의 공격으로 체력 감소
            current_health -= attacks[attack_index][1]
            attack_index += 1
            # 공격 받으면 연속 성공 시간 초기화
            consecutive_success = 0
            
            # 캐릭터가 죽으면 -1 반환
            if current_health <= 0:
                return -1
        
        else:
            # 공격받지 않았을 때는 붕대 감기 기술을 사용
            current_health += x  # 초당 회복량 만큼 회복
            current_health = min(current_health, max_health)  # 최대 체력 초과 방지
            consecutive_success += 1  # 연속 성공 시간 증가
            
            # 연속 성공 시간이 t초에 도달하면 추가 회복량을 적용하고 연속 성공 초기화
            if consecutive_success == t:
                current_health += y  # 추가 회복량 적용
                current_health = min(current_health, max_health)  # 최대 체력 초과 방지
                consecutive_success = 0  # 연속 성공 초기화

    return current_health  # 모든 공격이 끝난 후 남은 체력 반환