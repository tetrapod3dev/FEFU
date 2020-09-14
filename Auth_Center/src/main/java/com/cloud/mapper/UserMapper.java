package com.cloud.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.cloud.domain.UserDto;

@Mapper
public interface UserMapper {
	public UserDto findByUsername(String username);
}
