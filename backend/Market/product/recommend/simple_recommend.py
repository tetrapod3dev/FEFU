def recom_simple(user, merged_df, user_view_boolean, n_items=20):
    """
        유저와 같은 성별, 연령대인 다른 유저들의 평균 조회수를 기준으로
        가장 높은 평균 조회수를 가진 카테고리 목록을 리턴합니다.
        Params:
            user: 추천을 하고자 하는 유저입니다. (유저의 성별, 연령대가 포함되어있습니다.)
            merged_df: df_counts와 df_users를 user를 기준으로 merge한 DataFrame입니다.
            user_view_boolean: user가 조회한 항목이 있는지 확인하기 위한 변수입니다.
            n_items: 몇 개의 카테고리를 리턴할지 정하는 변수입니다.
        Returns:
            group_view_df: 추천할 카테고리와 평균 조회수가 담긴 pandas DataFrame입니다.
    """
    mask_age = merged_df['age']==user['age']
    mask_gender = merged_df['gender']==user['gender']

    view_df = merged_df[mask_age & mask_gender]

    grouped_view_df = (view_df.groupby(['category'])['sum']
                       .agg(['sum'])
                       .sort_values(by=['sum'], ascending=False)
                       .apply(lambda x: x / len(view_df['user'].unique())))

    if user_view_boolean:
        # 추천하고자하는 사용자가 조회한 항목이 있다면, 그를 추천 결과에 반영해줍니다.

        # 추천하고자하는 유저의 조회 데이터를 DataFrame으로 만들어줍니다.
        cur_user_data = (merged_df[merged_df['user']==user['username']]
                        .set_index('category')
                        .drop(columns=['user', 'gender', 'age']))

        # 그룹화 추천 결과와 유저 정보를 더합니다.
        # 예측값 : 개인이 조회한 횟수 + 유저 그룹이 평균적으로 조회한 횟수
        grouped_view_df = (grouped_view_df.add(cur_user_data, fill_value=0)
                        .sort_values(by='sum', ascending=False))

    grouped_view_df = grouped_view_df.reset_index()[:n_items]

    return grouped_view_df