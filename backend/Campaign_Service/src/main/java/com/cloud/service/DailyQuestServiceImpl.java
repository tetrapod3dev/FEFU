package com.cloud.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.cloud.domain.DailyQuestDto;
import com.cloud.mapper.DailyQuestMapper;

@Service
public class DailyQuestServiceImpl implements DailyQuestService {

	@Autowired
	private DailyQuestMapper questMapper;

	@Override
	public List<DailyQuestDto> findAll() {
		return questMapper.findAll();
	}

	@Override
	public List<DailyQuestDto> findByCompleteList(String username) {
		return questMapper.findByCompleteList(username);
	}

	@Override
	public int insertComplete(String username, int no) {
		questMapper.updateExp(username);
		return questMapper.insertComplete(username, no);
	}

}
