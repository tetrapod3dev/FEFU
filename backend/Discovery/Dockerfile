FROM openjdk:8-jdk-alpine

VOLUME /a402

ARG JAR_FILE=target/*.jar

COPY ${JAR_FILE} /home/ubuntu/builds/discovery/discover-v1.jar

ENTRYPOINT ["java", "-jar", "/home/ubuntu/builds/discovery/*.jar"