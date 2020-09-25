package com.cloud.controller;

import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;

import com.cloud.domain.DailyQuestDto;
import com.cloud.service.DailyQuestService;

import springfox.documentation.annotations.ApiIgnore;

@RestController
public class DailyQuestController {
	
	private static final Logger logger = LoggerFactory.getLogger(DailyQuestController.class);

	@Autowired
	private DailyQuestService questService;

	@GetMapping(value = "/daily-quest")
	public ResponseEntity<List<DailyQuestDto>> getTotalList() {
		List<DailyQuestDto> list = questService.findAll();
		return new ResponseEntity<List<DailyQuestDto>>(list, HttpStatus.OK);
	}

	@GetMapping(value = "/daily-quest/detail")
	public ResponseEntity<List<DailyQuestDto>> getCompletelist(@ApiIgnore @RequestHeader("X-USERNAME") String username) {
		logger.info(username + "--------------------");
		List<DailyQuestDto> list = questService.findByCompleteList(username);
		return new ResponseEntity<List<DailyQuestDto>>(list, HttpStatus.OK);
	}
	
	@PostMapping(value = "/daily-quest")
	public ResponseEntity<String> completeQuest(@RequestBody Map<String, Integer> data, @ApiIgnore @RequestHeader("X-USERNAME") String username){
		int no = data.get("quest_no");
		logger.info(no + " " + username);
		int res = questService.insertComplete(username, no);
		if(res == 0) {
			return new ResponseEntity<String>("완료 실패", HttpStatus.OK);
		}
		return new ResponseEntity<String>("완료 성공", HttpStatus.OK);
	}
}
