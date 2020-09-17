package com.cloud.service;

import java.util.List;

import com.cloud.domain.DailyQuestDto;

public interface DailyQuestService {
	
	public List<DailyQuestDto> findAll();
	public List<DailyQuestDto> findByCompleteList(String username);
	public int insertComplete(String username, int no);

}
