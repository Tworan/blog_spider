'''
用户表：
    uid: 用户id     主键
    User_name: 用户姓名     字符串类型
    User_passwd: 用户密码   字符串类型
    followings: 平台用户关注的微博博主      [博主1, 博主2， ....] 外键，多对多关系 对应到微博用户表中的blog_id
    potential_followings: 用户潜在的感兴趣的博主    [博主1, 博主2， ....] 外键，多对多关系  对应到微博用户表中的blog_id

    用户表对微博用户表进行见

动态表：
    text: 所有的动态信息，包括相关用户的相关微博     字符串类型

    动态表会进行每日清零

用户关注映射表：
    平台用户: 外键
    微博用户: 外键  到整个系统用户关注表

潜在关注映射表：
    平台用户: 外键
    微博用户: 外键  到整个系统用户关注表
    

整个系统关注用户表:
    所有关注用户: 

微博用户表：
    blog_user_name: 昵称
    activations: 动态   外键 对应到
    follows_counts: 关注数
    description: 用户描绘
    verified_reason: 个人认证

    微博用户表会每日保持静止，支持拓展

热榜表：
    id: 主键
    hotboard_info: 热榜内容
    plat: 平台


'''
