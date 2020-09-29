package com.cloud.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.UserDto;

@Mapper
public interface UserMapper {
	
	public UserDto findByUsername(String username);
	public int userRegistier(UserDto dto);
	public int updateUser(UserDto dto);
	public int changePassword(String password, String username);
	public int checkByUsername(String usernmae);
	public int checkByNickname(String nickname);
	public int insertUserRole(String usernmae);
}
