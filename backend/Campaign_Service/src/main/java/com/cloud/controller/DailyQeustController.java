package com.cloud.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cloud.domain.DailyQuestDto;
import com.cloud.service.DailyQuestService;

@RestController
public class DailyQeustController {

	@Autowired
	private DailyQuestService questService;

	@GetMapping(value = "/daily-quest")
	public ResponseEntity<List<DailyQuestDto>> getTotalList() {
		List<DailyQuestDto> list = questService.findAll();
		return new ResponseEntity<List<DailyQuestDto>>(list, HttpStatus.OK);
	}
}
