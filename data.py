class Data:
    order_create_body_valid = {"ingredients": ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6f",
                                               "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa6d"]}
    order_create_body_invalid = {"ingredients": ["1c0c5a71d1f82001bdaaa75", "1c0c5a71d1f82001bdaaa6f",
                                                 "1c0c5a71d1f82001bdaaa76", "1c0c5a71d1f82001bdaaa6d"]}
    order_create_body_empty_ingredients = {"ingredients": []}
    order_create_empty_ingredients_response = {"success": False, "message": "Ingredient ids must be provided"}

    user_create_random_body_valid = {"email": "defaultemail@stellarburgers.com", "password": "password",
                                     "name": "Username"}
    user_create_body_invalid = {"password": "password", "name": "Username"}
    user_create_already_exists_response = {"success": False, "message": "User already exists"}
    user_create_body_invalid_response = {"success": False, "message": "Email, password and name are required fields"}
    user_login_not_exist_data = {"email": "narochnonepridumaesh@takoi.email", "password": "password"}
    user_login_not_exist_response = {"success": False, "message": "email or password are incorrect"}

    user_not_authorized_response = {"success": False, "message": "You should be authorised"}
